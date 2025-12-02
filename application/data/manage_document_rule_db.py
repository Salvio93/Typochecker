import sqlite3
from sqlite3 import Error


def link_rule_and_doc(document_id,rule_id,category_id,start,end,idx,lenght,detected=0,db_file='./application/data/DB/TypoChecker.db'):
    try:
        con= sqlite3.connect(db_file)
        cur = con.cursor()
        sqlite_insert_blob_query = """ INSERT INTO document_rules
                                        (document_id, rule_id,category_id, start , end , idx , lenght, detected ) VALUES (?,?, ?, ?, ?,?,?,?)"""
        
        # Convert data into tuple format
        data_tuple = (document_id,rule_id,category_id,start,end,idx,lenght,detected)
        cur.execute(sqlite_insert_blob_query, data_tuple)
        con.commit()
        #print("Data inserted successfully into a table")

    except sqlite3.Error as error:
        print("Failed to insert data into table", error)
    



def remove_docu_rule_db_by_document_id(document_id,db_file='./application/data/DB/TypoChecker.db'):
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        cur.execute("DELETE FROM document_rules WHERE document_id=?;",(document_id,))
        con.commit()
        #print('Deleted data!')
    except Error as e:
        print(e)
    
def remove_docu_rule_db_by_document_rule_id(document_rule_id,db_file='./application/data/DB/TypoChecker.db'):
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        cur.execute("DELETE FROM document_rules WHERE document_rule_id=?;",(document_rule_id,))
        con.commit()
        #print('Deleted data!')
    except Error as e:
        print(e)

def remove_docu_rule_db_by_document_rule_id_conn(document_rule_id,db_conn):
    try:
        cur = db_conn.cursor()
        cur.execute("DELETE FROM document_rules WHERE document_rule_id=?;",(document_rule_id,))
        db_conn.commit()
        #print('Deleted data!')
    except Error as e:
        print(e)
    
def update_document_rule_db(document_rule_id,new_end,new_idx,db_file='./application/data/DB/TypoChecker.db'):
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        cur.execute("UPDATE document_rules SET end=?, idx=? WHERE document_rule_id = ?;",
                    (new_end,new_idx,document_rule_id))
        con.commit()
    except Error as e:
        print("couldn't update docu rule",e)

def update_document_rule_db_conn(document_rule_id,new_end,new_idx, db_conn):
    try:
        cur = db_conn.cursor()
        cur.execute("UPDATE document_rules SET end=?, idx=? WHERE document_rule_id = ?;",
                    (new_end,new_idx,document_rule_id))
        db_conn.commit()
    except Error as e:
        print("couldn't update docu rule",e)

def update_document_rule_db_conn_no_commit(document_rule_id,new_end,new_idx, db_conn):
    try:
        cur = db_conn.cursor()
        cur.execute("UPDATE document_rules SET end=?, idx=? WHERE document_rule_id = ?;",
                    (new_end,new_idx,document_rule_id))
    except Error as e:
        print("couldn't update docu rule",e)


def print_docu_rule_db(db_file='./application/data/DB/TypoChecker.db'):
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        res = cur.execute("SELECT * FROM document_rules;")

        print(res.fetchall())
    except Error as e:
        print(e)


def retrieve_docu_rule_list(document_rule_id,db_file='./application/data/DB/TypoChecker.db'):
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        res = cur.execute("SELECT * FROM document_rules WHERE document_rule_id=?;",(document_rule_id,))
        return res.fetchall()
    except Error as e:
                print(e)



def retrieve_docu_rule_list_by_document_id(document_id,db_file='./application/data/DB/TypoChecker.db'):
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        res = cur.execute("SELECT * FROM document_rules WHERE document_id=?;",(document_id,))
        return res.fetchall()
    except Error as e:
                print("Failed to retrieve docu_rule_list_by_document_id",e)


def retrieve_docu_rule_list_by_document_id_conn(document_id, db_conn):
    try:
        cur = db_conn.cursor()
        res = cur.execute("SELECT * FROM document_rules WHERE document_id=?;",(document_id,))
        return res.fetchall()
    except Error as e:
                print("Failed to retrieve docu_rule_list_by_document_id",e)


def retrieve_docu_rule_list_by_document_id_where_correction(document_id,db_file='./application/data/DB/TypoChecker.db'):
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        res = cur.execute("SELECT * FROM document_rules WHERE document_id=? AND detected=0;",(document_id,))
        out = res.fetchall()
        res.close()
        return out 
    except Error as e:
                print("Failed to retrieve docu_rule_list_by_document_id",e)

