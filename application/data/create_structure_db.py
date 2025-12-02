import sqlite3
from sqlite3 import Error


def create_all(db_file='./application/DB/TypoChecker.db'):
    con = None
    try:
        con = sqlite3.connect(db_file)
        print(sqlite3.version)
        create_structure(con)
    except Error as e:
        print(e)
    finally:
        if con:
            con.close()

def create_structure(con):
    cur = con.cursor()
    #cur.execute("CREATE TABLE users(user_id INTEGER PRIMARY KEY AUTOINCREMENT,username text NOT NULL UNIQUE, email text, password NOT NULL, role NOT NULL)")
    cur.execute("CREATE TABLE category(category_id INTEGER PRIMARY KEY AUTOINCREMENT,category_name text NOT NULL)")
    cur.execute("CREATE TABLE rules(rule_id INTEGER PRIMARY KEY AUTOINCREMENT,category_id INTEGER NOT NULL,name text NOT NULL, description text, bad_typo text NOT NULL, good_typo text NOT NULL, FOREIGN KEY(category_id) REFERENCES category(category_id) ON UPDATE CASCADE ON DELETE SET NULL)")
    cur.execute("CREATE TABLE documents(document_id INTEGER PRIMARY KEY AUTOINCREMENT,  user_id INTEGER NOT NULL, title text NOT NULL,last_modif INTEGER NOT NULL, autor INTEGER NOT NULL, creation INTEGER NOT NULL, path text NOT NULL, FOREIGN KEY(user_id) REFERENCES users (user_id) ON UPDATE CASCADE ON DELETE SET NULL)")
    #cur.execute("CREATE TABLE document_corrections(correction_id INTEGER PRIMARY KEY AUTOINCREMENT,name text NOT NULL, description text, bad_typo text NOT NULL, good_typo text NOT NULL)")
    cur.execute("CREATE TABLE document_rules(document_rule_id INTEGER PRIMARY KEY AUTOINCREMENT, document_id INTEGER NOT NULL,rule_id INTEGER NOT NULL,category_id INTEGER NOT NULL, start INTEGER NOT NULL,end INTEGER NOT NULL ,idx INTEGER NOT NULL,lenght INTEGER NOT NULL , detected INTEGER , FOREIGN KEY(document_id) REFERENCES documents(document_id) ON UPDATE CASCADE ON DELETE SET NULL, FOREIGN KEY(rule_id) REFERENCES rules(rule_id) ON UPDATE CASCADE ON DELETE SET NULL, FOREIGN KEY(category_id) REFERENCES category(category_id) ON UPDATE CASCADE ON DELETE SET NULL)")

