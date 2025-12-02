import spacy
from .rule_manager import *
from .document_manager import *
from .manage_document_rule_db import *


nlp = spacy.load("fr_core_news_sm")


list_of_sent_ending=[".",":",";","...","?","!",","]
unos = ['un','deux','trois','quatre','cinque','six','sept','huit','neuf','1','2','3','4','5','6','7','8','9']
list_of_num = ['dix','vingt','trente','quarante','cinquante','soixante','septante','quatre-vingt','nonante','cent','mille','million','milliard']



"""
function to find rules appliable in a text (from a document)
----
String texte : text to search into
Integer document_id : id of the document stored in the database that we want to analyze
----
DB CHANGE : add rule related to text (text of a document), into the document_rule TABLE
----
author: Salvio Strazzante   
date: 11/04
"""
def detect_bad_paragraph(text,document_id, dbp='./application/data/DB/TypoChecker.db'):
    #plutôt que de faire un appel à la db
    list_of_bad_typo=[e.get_bad_typo().lower() for e in list_of_rules_obj]
    
    doc = nlp(text)
    last_token = ""
            
    for sent in doc.sents:
        #detect lack of punct
        if (sent.text[-1] not in list_of_sent_ending):
            try:
                if ((sent.text[-1]=="" or sent.text[-1]==" ") and sent.text[-2] not in list_of_sent_ending):
                    #print("Ne manquerait-t-il pas un point à la fin de la phrase : " , sent.text)
                    link_rule_and_doc(document_id,-1,5,sent.start_char,sent.end_char-1,sent.end_char-1,1,1,dbp)

            except:
                print('')

        for token in sent:

            modif_idx = 0
            modif_len =0


            if (' '+token.text.lower()+' ' in list_of_bad_typo and text[token.idx+1]==' '  and text[token.idx-1]==' ' ):
                index = list_of_bad_typo.index(' '+token.text.lower()+' ')
                rule_id = list_of_rules_obj[index].get_id()
                cat_id = list_of_rules_obj[index].get_cat()
                modif_idx = -1 
                modif_len = 2

                link_rule_and_doc(document_id,rule_id,cat_id,sent.start_char,sent.end_char-1,token.idx+modif_idx,len(token.text)+modif_len,0,dbp)
                
            else:
                if (token.text.lower()+' ' in list_of_bad_typo and text[token.idx+1]==' ' and text[token.idx-1]!=' '  ):
                    index = list_of_bad_typo.index(token.text.lower()+' ')
                    rule_id = list_of_rules_obj[index].get_id()
                    cat_id = list_of_rules_obj[index].get_cat()


                    modif_len = 1
                    link_rule_and_doc(document_id,rule_id,cat_id,sent.start_char,sent.end_char-1,token.idx+modif_idx,len(token.text)+modif_len,0,dbp)
                    

                elif (' '+token.text.lower() in list_of_bad_typo and text[token.idx-1]==' 'and text[token.idx+1]!=' '  ):
                    index = list_of_bad_typo.index(' '+token.text.lower())
                    rule_id = list_of_rules_obj[index].get_id()
                    cat_id = list_of_rules_obj[index].get_cat()

                    modif_idx =-1
                    modif_len =1
                    link_rule_and_doc(document_id,rule_id,cat_id,sent.start_char,sent.end_char-1,token.idx+modif_idx,len(token.text)+modif_len,0,dbp)
                elif (token.text.lower() in list_of_bad_typo ):
                    index = list_of_bad_typo.index(token.text.lower())
                    rule_id = list_of_rules_obj[index].get_id()
                    cat_id = list_of_rules_obj[index].get_cat()
                    
                    link_rule_and_doc(document_id,rule_id,cat_id,sent.start_char,sent.end_char-1,token.idx+modif_idx,len(token.text)+modif_len,0,dbp)
                else:

                    #detect number 
                    if (token.text in list_of_num or token.text.split('-')[0] in list_of_num or (token.text.isdigit() and len(token.text)>=4)):
                        #print('potential num error :'+token.text)
                        link_rule_and_doc(document_id,-2,6,sent.start_char,sent.end_char-1,token.idx,len(token.text),1,dbp)


                    #detect guillement anglais et fr
                    if (token.text in ['"','«','»',"'"]):
                        #print('potential guillemet error :'+token.text)
                        link_rule_and_doc(document_id,-3,7,sent.start_char,sent.end_char-1,token.idx,len(token.text),1,dbp)


                
                    #liste à puce

                    #tiret trait d'union

                    #detect potential maj issue
                    if (token.text!=token.text.lower() and (last_token not in list_of_sent_ending and last_token != " "and last_token != "\n" and last_token !="")):
                        #print('potential maj error :'+token.text + '---'+last_token)
                        link_rule_and_doc(document_id,-4,8,sent.start_char,sent.end_char-1,token.idx,len(token.text),1,dbp)

                    if (token.text[0] in ['A','E','C'] and (token.text[0]== 'C' and token.text[1] in ['a','e','i','o','u','y'])):
                        #print('potential É,À,Ç type error :'+token.text)
                        link_rule_and_doc(document_id,-5,9,sent.start_char,sent.end_char-1,token.idx,len(token.text),1,dbp)


                    #detect double token 
                    if (last_token == token.text.lower()):
                        #print(sent.text+' -   double token at: ',token.idx)
                        #print('last token:'+last_token+' - current token: '+token.text.lower())
                        link_rule_and_doc(document_id,-6,10,sent.start_char,sent.end_char-1,token.idx,len(token.text),1,dbp)

            last_token = token.text.lower()



"""
function to apply a rule correction in a text
----
String texte : text to correct
Integer document_rule_id : stored appliable rule that we now want to apply
----
String text_corrected : text corrected  ->>> soon to be a write in a docx file
----
author: Salvio Strazzante   
date: 21/03
"""
def correct_bad_paragraph(text,document_rule_id):
    error_data = retrieve_docu_rule_list(document_rule_id)[0]
    document_id = error_data[1]
    modif_doc=retrieve_doc_list(document_id)[0]

    rule_id = error_data[2]

    error_localisation = error_data[6]
    error_lenght = error_data[7]
    correct_rule = retrieve_rules_by_id(rule_id)
    bad_typo = correct_rule[4]
    correction = correct_rule[5]

    diff_in_len = len(correction)-len(bad_typo)

    text_corrected = text[:error_localisation] + correction + text[error_localisation +error_lenght:]

    
    correct_indexes(document_rule_id,diff_in_len,error_localisation+error_lenght,document_id)

    return text_corrected

"""
function to adjust all the index of the previously found error (applying a rule and transforming 'x' into 'xxxx' shift everything)
----
Integer document_rule_id : stored appliable rule that we now want to apply
Integer diff_in_len : diff in length between bad_typo.length and good_typo.length
Integer error_localisation : idx of the first char of the bad_typo found in the text
Integer document_id : id of the file we are currently working on (file where rule in docu_rule table is being applied to)
----
DB CHANGE : end and idx
----
author: Salvio Strazzante   
date: 11/04
"""
def correct_indexes(document_rule_id,diff_in_len,error_localisation,document_id, dbp='./application/data/DB/TypoChecker.db', remove_rule=True):
    
    #delete specific doc rule after correction in text
    if remove_rule:
        remove_docu_rule_db_by_document_rule_id(document_rule_id, dbp)

    #get all rules applyable for doc
    all_rule_of_doc = retrieve_docu_rule_list_by_document_id(document_id, dbp)
    #modify end,idx for those rules
    for rule in all_rule_of_doc:
        #si regle se trouve a un index > à celui de la regle qui viens d'etre appliqué alors décaler
        if (rule[6] >= error_localisation):
            update_document_rule_db(rule[0],rule[5]+diff_in_len,rule[6]+diff_in_len)


def correct_indexes_conn(document_rule_id,diff_in_len,error_localisation,document_id, db_conn, remove_rule=True):

    #delete specific doc rule after correction in text
    if remove_rule:
        remove_docu_rule_db_by_document_rule_id_conn(document_rule_id, db_conn)

    #get all rules applyable for doc
    all_rule_of_doc = retrieve_docu_rule_list_by_document_id_conn(document_id, db_conn)
    
    #modify end,idx for those rules
    for rule in all_rule_of_doc:
        #si regle se trouve a un index > à celui de la regle qui viens d'etre appliqué alors décaler
        if (rule[6] >= error_localisation):
            update_document_rule_db_conn_no_commit(rule[0],rule[5]+diff_in_len,rule[6]+diff_in_len, db_conn)

    db_conn.commit()