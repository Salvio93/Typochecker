########################
# Data base and rules  #
########################
import sys
import io
sys.path.append('../')

from data.rule_manager import *
from data.document_manager import *
from data.manage_document_rule_db import *
from data.create_structure_db import *
from data.main import *
#from application.data.depreciated_get_set_docx import *

#########
# Flask #
#########
import os
import flask
from flask import Flask, request, render_template, flash
from flask import redirect,url_for, jsonify, session
from flask import json

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired
from wtforms.widgets import TextArea

from threading import Lock

#######################
# Document management #
#######################
from docx import Document
from hashlib import sha256


###############################
# Session and data management #
###############################

# tmp data base containing the data of the current session
sessions_data = {}

# info of a current session
class SessionData:
    def __init__(self):
        self.raw_file = None
        self.current_file_id = None
        
        self.review_start = None
        self.review_end = None

        self.current_rule = None
        self.rule_type = None
        self.rule_name = None

        self.hist = []


# helper session to retrieves session info
def get_session_data(session_) -> SessionData:
    return sessions_data[session_["uid"]]

############
# UI Forms #
############
class AddRuleForm(FlaskForm):
    name = StringField('Nom',
                       validators=[InputRequired('Le champ Nom est nécéssaire')])
    cat_id = StringField('Catégorie de régle', widget=TextArea())

    desc = StringField('Déscription', 
                       widget=TextArea())
    good = StringField('Bonne typographie', widget=TextArea())
    bad  = StringField('Mauvaise typographie', widget=TextArea())
    
    submit = SubmitField(label='Validez')


class ModifRuleForm(FlaskForm):
    name = StringField('Nom',
                       validators=[InputRequired('Le champ Nom est nécéssaire')])
    cat_id = StringField('Catégorie de régle', widget=TextArea())

    desc = StringField('Déscription', 
                       widget=TextArea())
    good = StringField('Bonne typographie', widget=TextArea())
    bad  = StringField('Mauvaise typographie', widget=TextArea())
    
    submit = SubmitField(label='Validez')


# router
app = Flask(__name__)
app.config.from_object(__name__)

# shared db con
import sqlite3
from flask import g

DATABASE = './application/data/DB/TypoChecker.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# setup a uid
@app.before_request
def set_uid():
    # check if the session has an id, if not give one
    if "uid" not in session or \
        session["uid"] not in sessions_data:
        uid = os.urandom(256)
        
        while uid in sessions_data:
            uid = os.urandom(256)

        session["uid"] = uid
        sessions_data[uid] = SessionData()


# File Management
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route('/post_file', methods=['POST'])
def post_file():
    try:
        # Get file from request
        file = request.files['docxFile']
        get_session_data(session).raw_file = file.stream.read()

        # Check if the file has a .docx extension
        if file and file.filename.endswith('.docx'):
            text = ''.join( ((par.text+'\n') if len(par.text) > 0 else "") for par in Document(file).paragraphs)
            file_hash = sha256(text.encode()).digest()[:7]
            file_id = int.from_bytes(file_hash, byteorder='big')
            

            get_session_data(session).current_text = text
            get_session_data(session).current_file_id = file_id
            get_session_data(session).hist = []
            
            get_file_from_db(file_id)

            # clean previous error if left
            clean_errors()

            detect_bad_paragraph(text, file_id, './application/data/DB/TypoChecker.db')
            
            #add highlight
            #set_all_hightlight_of_doc(file_id)

            return redirect('/doc_en_lec')
        else:
            flash('Veuillez sélectionner un fichier DOCX valide.', 'error')
            return redirect(url_for('home')) 
    
    except Exception as e:
        flash('Erreur ' + str(e), 'error')
        return redirect(url_for('home'))


@app.route('/comment_file', methods=['POST'])
def comment_file():
    try:
        # Get text
        text= request.form["comment"]
        #create file
        with open("./application/data/test.txt", "w") as file:
            file.write(text)

    
            try:
                file_hash = sha256(text.encode()).digest()[:7]
                file_id = int.from_bytes(file_hash, byteorder='big')

                get_session_data(session).current_text = text
                get_session_data(session).current_file_id = file_id
                get_session_data(session).hist = []
                
                get_file_from_db(file_id)

                detect_bad_paragraph(text, file_id, './application/data/DB/TypoChecker.db')
                
                #add highlight
                #set_all_hightlight_of_doc(file_id)

                return redirect('/doc_en_lec')
            except Exception as e:
                flash('Veuillez sélectionner un fichier text valide.'+str(e), 'error')
                return redirect(url_for('home')) 
    
    except Exception as e:
        flash('Erreur ' + str(e), 'error')
        return redirect(url_for('home'))



@app.route('/doc_en_lec', methods=['POST', 'GET'])
def edit_ui():
    return render_template('doc_en_lec.html') 


# Rule management
@app.route('/rules', methods=['POST', 'GET'])
def rules():
    return render_template('rules.html', rules=list_of_rules_obj,list_of_cat=retrieve_category_db())

@app.route('/delete_rule/<int:rule_id>')
def delete_rule_route(rule_id):
    delete_rule(list_of_rules_obj[rule_id-1],
                 db_file="application/data/DB/TypoChecker.db")
    return redirect(url_for('rules'))


@app.route('/ajout', methods=['POST', 'GET'])
def ajout():
    form = AddRuleForm()
    
    if form.validate_on_submit():
        add_rule(form.name.data, form.desc.data, 
                 form.bad.data, form.good.data,form.cat_id.data,
                  db_file="application/data/DB/TypoChecker.db")
        return redirect(url_for('rules'))
    return render_template('ajout.html', form=form, url="ajout", list_of_cat=retrieve_category_db())


@app.route('/modify_rule/<int:rule_id>', methods=['POST', 'GET'])
def modify_rule_route(rule_id):
    form = ModifRuleForm()
    if list_of_rules_obj[rule_id-1] and not form.validate_on_submit():
        form.name.data = list_of_rules_obj[rule_id-1].get_name()
        form.cat_id.data = list_of_rules_obj[rule_id-1].get_cat()
        form.desc.data = list_of_rules_obj[rule_id-1].get_description()
        form.good.data = list_of_rules_obj[rule_id-1].get_good_typo()
        form.bad.data = list_of_rules_obj[rule_id-1].get_bad_typo()
        
    if form.validate_on_submit():
        modify_rule(list_of_rules_obj[rule_id-1],
                    form.name.data, form.desc.data, 
                    form.bad.data, form.good.data,form.cat_id.data,
                    db_file="application/data/DB/TypoChecker.db")
        return redirect(url_for('rules'))
    return render_template('modif.html', form=form, url="/modify_rule/" + str(rule_id),list_of_cat=retrieve_category_db())


# rapport and file generation
@app.route("/rapport")
def rapport():
    return render_template('rapport.html')


# API 
@app.route('/api/get_rules')
def get_rules():
    return jsonify([(rule.get_id(),rule.get_cat(), rule.get_name(), 
                     rule.get_description(), rule.get_bad_typo(), rule.get_good_typo()) 
                    for rule in list_of_rules_obj])


@app.route('/api/get_all_corrections')
def get_all_coorections():
    # get session data
    if session["uid"] not in sessions_data: return jsonify("Selectioner un document dans la page d'acceuil")
    file_id = get_session_data(session).current_file_id
    
    # get error data
    errors_data = retrieve_docu_rule_list_by_document_id(file_id, './application/data/DB/TypoChecker.db')
    if len(errors_data) < 1: return jsonify([])
    
    # resturcture data
    data = []

    for error in errors_data:
        error_data = error_2_dict(error)
        if (error_data["detected"]==0):
            correct_rule = retrieve_rules_by_id(error_data["rule_id"], './application/data/DB/TypoChecker.db')
            rule_dict = rule_2_dict(correct_rule)

            data.append({"error": error_data, "rule": rule_dict})
        else:
            data.append({"error": error_data, "rule": { "rule_id":  error_data["rule_id"],
            "cat_id":error_data["category_id"],
             "name": error_data["rule_id"]
             } })


    return jsonify(data)



@app.route('/api/accept_change_<int:rule_id>', methods=["GET"])
def accept_change_id(rule_id):
    try:
        file_id = get_session_data(session).current_file_id
        get_all_coorections = retrieve_docu_rule_list_by_document_id_where_correction(file_id, './application/data/DB/TypoChecker.db')

        for correction in get_all_coorections:
            correction = error_2_dict(correction)
            
            if correction['document_rule_id'] == rule_id:
                correct_rule = retrieve_rules_by_id(correction["rule_id"], './application/data/DB/TypoChecker.db')
                rule_dict = rule_2_dict(correct_rule)


                text = get_session_data(session).current_text
                text = text[:correction['idx']] + rule_dict['good_typo'] + text[correction['idx']+len(rule_dict['bad_typo']):]
                get_session_data(session).current_text = text

                correct_indexes_conn(rule_id, (len(rule_dict['good_typo'])-len(rule_dict['bad_typo'])), 
                                correction['idx'], file_id, get_db())

    except Exception as e:
        print(e)

    return jsonify("")


@app.route('/api/refuse_change_<int:rule_id>', methods=["GET"])
def refuse_change(rule_id):
    try:
        file_id = get_session_data(session).current_file_id
        get_all_coorections = retrieve_docu_rule_list_by_document_id_where_correction(file_id, './application/data/DB/TypoChecker.db')

        for correction in get_all_coorections:
            correction = error_2_dict(correction)
            
            if correction['document_rule_id'] == rule_id:
                correct_indexes_conn(rule_id, 0, 
                                correction['idx'], file_id, get_db())

    except Exception as e:
        print(e)

    return jsonify("")

@app.route('/api/end_review', methods=["POST"])
def end_review():
    request_data = request.get_json()
    get_session_data(session).current_text = request_data

    return clean_errors()

def clean_errors():
    try:
        file_id = get_session_data(session).current_file_id
        get_all_coorections = retrieve_docu_rule_list_by_document_id_where_correction(file_id, './application/data/DB/TypoChecker.db')

        for correction in get_all_coorections:
            correction = error_2_dict(correction)
            remove_docu_rule_db_by_document_rule_id(correction['document_rule_id'], './application/data/DB/TypoChecker.db')

    except Exception as e:
        print(e)

    return jsonify("")



@app.route('/api/ignore_rule', methods=["POST"])
def ignore_rule():
    try:
        # retrieve data
        rules  = retrieve_docu_rule_list_by_document_id_where_correction(get_session_data(session).current_file_id, 
                                                        './application/data/DB/TypoChecker.db')
        rule_type = get_session_data(session).rule_type

        # delete error from that rule
        for rule in rules:
            if (rule[2] == rule_type):
                remove_docu_rule_db_by_document_rule_id(rule[0], 
                                                        './application/data/DB/TypoChecker.db')

    except Exception as e:
        print(e)

    return jsonify("")


@app.route('/api/get_text')
def get_text():
    try:
        return jsonify(get_session_data(session).current_text)
    except:
        return jsonify('')

@app.route('/api/dl_file.txt')
def dl_txt_file():
    fp = io.BytesIO(get_session_data(session).current_text.encode())
    return  flask.send_file(fp,  mimetype='text/plain')


@app.route('/api/dl_file.docx')
def dl_file():
    file_id = get_session_data(session).current_file_id
    tmp_file_name = "tmp/%d.docx" %file_id

    with open(tmp_file_name, "wb") as fp:
        fp.write(get_session_data(session).raw_file)

    setText(get_session_data(session).current_text, tmp_file_name)

    with open(tmp_file_name, "rb") as fp:
        txt = io.BytesIO(fp.read())
    os.remove(tmp_file_name)
    
    return  flask.send_file(txt,  mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')

update_text_lock = Lock()
@app.route('/api/update_text', methods=["POST"])
def update_text():
        try:
            with update_text_lock:
                text = request.json
                get_session_data(session).current_text = text
                clean_errors()
                detect_bad_paragraph(text, get_session_data(session).current_file_id , './application/data/DB/TypoChecker.db')

        except Exception as e:
            print(e)
            
       
        return jsonify("")


# extract and format db data
def rule_2_dict(rule):
    return { "rule_id":  rule[0],
            "cat_id":rule[1],
             "name": rule[2],
             "description": rule[3],
             "bad_typo": rule[4],
             "good_typo": rule[5]
             }

def error_2_dict(error):
    return {"document_rule_id": error[0],
            "document_id": error[1],
            "rule_id": error[2],
            "category_id": error[3],
            "start": error[4],
            "end": error[5],
            "idx": error[6],
            "lenght": error[7],
            "detected": error[8]}