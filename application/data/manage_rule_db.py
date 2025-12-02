import sqlite3
from sqlite3 import Error


def add_rule_to_db(name,description,bad_typo,good_typo,cat_id,db_file):
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        cur.execute("INSERT INTO rules (category_id,name, description, bad_typo,good_typo) values (?, ?, ?, ?,?)",
                (cat_id,name,description,bad_typo,good_typo))
        con.commit()
    except Error as e:
        print(e)
        
def remove_rule_from_db(rule_id,db_file):
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        cur.execute("DELETE FROM rules where rule_id=?",(rule_id,))
        con.commit()
        #print('Deleted data!')
    except Error as e:
        print(e)
    
def modify_db(rule_id,new_name,new_description,new_bad_typo,new_good_typo,new_cat_id,db_file):
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        cur.execute("UPDATE rules SET  category_id=?, name= ?, description=?, bad_typo=?, good_typo=? WHERE rule_id = ?;",
                    (new_cat_id,new_name,new_description,new_bad_typo,new_good_typo,rule_id))
        con.commit()
    except Error as e:
        print(e)


def retrieve_rules_by_id(rule_id,db_file='./application/data/DB/TypoChecker.db'):
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        res = cur.execute("SELECT * FROM rules WHERE rule_id=?;",(rule_id,))
        list_of_rule = res.fetchone()
        res.close()
        return list_of_rule
    except Error as e:
                print(e)



def retrieve_rules_list(db_file='./application/data/DB/TypoChecker.db'):
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        res = cur.execute("SELECT * FROM rules;")
        list_of_rule = res.fetchall()
        return list_of_rule
    except Error as e:
                print(e)



def print_rule_db(db_file='./application/data/DB/TypoChecker.db'):
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        res = cur.execute("SELECT * FROM rules;")

        print(res.fetchall())
    except Error as e:
        print(e)


  