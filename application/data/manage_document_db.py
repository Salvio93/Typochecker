import sqlite3
from sqlite3 import Error

#add to document db
def add_doc_to_db(file_id,filename,metadata,path,db_file='./application/data/DB/TypoChecker.db'):
    last_modif = metadata[0]
    autor = metadata[1]
    creation = metadata[2]
    try:
        con= sqlite3.connect(db_file)
        cur = con.cursor()
        sqlite_insert_blob_query = """ INSERT INTO documents
                                        (document_id,user_id,title, last_modif, autor, creation , path   ) VALUES (?,?, ?, ?,?,?,?)"""

        
        # Convert data into tuple format
        data_tuple = (file_id,0,filename, last_modif, autor,creation,path)
        cur.execute(sqlite_insert_blob_query, data_tuple)
        con.commit()
        print("File inserted successfully into a table")

    except sqlite3.Error as error:
        print("Failed to insert into table", error)
    

def retrieve_doc_from_db(filename,metadata,path,db_file='./application/data/DB/TypoChecker.db'):
    last_modif = metadata[0]
    autor = metadata[1]
    creation = metadata[2]

    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()


        sql_fetch_blob_query = """SELECT * FROM documents WHERE title = ? AND last_modif = ? AND autor=?  AND creation=? AND path=? """
        cur.execute(sql_fetch_blob_query, (filename,last_modif, autor,creation,path))
        res = cur.fetchone()
        print("File retrieved successfully from a table")

        return res


    except sqlite3.Error as error:
        print("Failed to retreive from sqlite table", error)

    
def update_document_db(document_id,new_filename,new_last_modif,new_autor,new_creation,new_path,db_file='./application/data/DB/TypoChecker.db'):
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        cur.execute("UPDATE documents SET title=?, last_modif=?, autor=?,creation =?, path=? WHERE document_id = ?;",
                    (new_filename,new_last_modif,new_autor,new_creation,new_path,document_id))
        con.commit()
    except Error as e:
        print("couldn't update docu rule"+e)

def print_docu_db(db_file='./application/data/DB/TypoChecker.db'):
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        res = cur.execute("SELECT * FROM documents;")
        print(res.fetchall())
    except Error as e:
        print(e)




def retrieve_doc_list(document_id,db_file='./application/data/DB/TypoChecker.db'):
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        res = cur.execute("SELECT * FROM documents WHERE document_id=?;",(document_id,))
        return res.fetchall()
    except Error as e:
                print(e)




def retrieve_doc_list_by_path(path,db_file='./application/data/DB/TypoChecker.db'):
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        res = cur.execute("SELECT * FROM documents WHERE path=?;",(path,))
        return res.fetchall()
    except Error as e:
                print(e)
"""
def download_new_file():
    return

"""