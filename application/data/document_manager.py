from .manage_document_db import *
import docx



"""
Get the metadat of a doc with docx
---------
str doc : path of the doc
----------
dict metadata : metadata of this doc
"""
def getMetaData(doc):
    metadata = {}
    prop = doc.core_properties
    metadata["author"] = prop.author
    metadata["category"] = prop.category
    metadata["comments"] = prop.comments
    metadata["content_status"] = prop.content_status
    metadata["created"] = prop.created
    metadata["identifier"] = prop.identifier
    metadata["keywords"] = prop.keywords
    metadata["last_modified_by"] = prop.last_modified_by
    metadata["language"] = prop.language
    metadata["modified"] = prop.modified
    metadata["subject"] = prop.subject
    metadata["title"] = prop.title
    metadata["version"] = prop.version
    return metadata


"""
Get a file from the db or add it to the db and return it's info
--------------
str doc : path of the doc
---------------
list str : info of the doc stored in db
"""
def get_file_from_db(file_id,file_path='./application/data/test.docx'):


    filename = file_path.split('/')[-1]
  
    doc = docx.Document(file_path)

    metadata = getMetaData(doc)

    usefull_metadata = [metadata["modified"],metadata["author"],metadata["created"]]


    file_from_db =retrieve_doc_from_db(filename,usefull_metadata,file_path)

    if (file_from_db != None):
        return file_from_db

    else:
        add_doc_to_db(file_id,filename,usefull_metadata,file_path)

        file_from_db = retrieve_doc_from_db(filename,usefull_metadata,file_path)
        return file_from_db

