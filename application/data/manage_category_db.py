import sqlite3
from sqlite3 import Error

def add_category_to_db(category_name,db_file):
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        cur.execute("INSERT INTO category (category_name) values (?)",
                (category_name,))
        con.commit()
    except Error as e:
        print(e)
        
def add_category_to_db_and_id(category_id,category_name,db_file):
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        cur.execute("INSERT INTO category (category_id,category_name) values (?,?)",
                (category_id,category_name,))
        con.commit()
    except Error as e:
        print(e)
def remove_category_from_db(category_id,db_file):
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        cur.execute("DELETE FROM category where category_id=?",(category_id,))
        con.commit()
    except Error as e:
        print(e)
    
def modify_category(category_id,new_category_name,db_file):
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        cur.execute("UPDATE category SET category_name= ? WHERE category_id = ?;",
                    (new_category_name,category_id))
        con.commit()
    except Error as e:
        print(e)


def retrieve_category_by_id(category_id,db_file='./application/data/DB/TypoChecker.db'):
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        res = cur.execute("SELECT * FROM category WHERE category_id=?;",(category_id,))
        list_of_rule = res.fetchone()
        return list_of_rule
    except Error as e:
                print(e)


def retrieve_category_db(db_file='./application/data/DB/TypoChecker.db'):
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        res = cur.execute("SELECT * FROM category;")
        list_of_rule = res.fetchall()
        return list_of_rule
    except Error as e:
        print(e)


def print_category_db(db_file='./application/data/DB/TypoChecker.db'):
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        res = cur.execute("SELECT * FROM category;")

        print(res.fetchall())
    except Error as e:
        print(e)


