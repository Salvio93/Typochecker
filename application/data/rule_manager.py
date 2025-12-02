from .Rule import *
from .manage_rule_db import *


"""
function to add a new rule in the db (and [list_of_rule_obj])
----
sqlite3.Connection con
String name : name of the rule
String description : description of the rule
String bad_typo : the words/punctuations/... in the text that need to be corrected
String good_typo : the correction to apply in the text (to said bad_typo ^)
----
----
author: Salvio Strazzante   
date: 08/03
"""
def add_rule(name,description,bad_typo,good_typo,cat_id=0,db_file='./application/data/DB/TypoChecker.db'):
    
    add_rule_to_db(name,description,bad_typo,good_typo,cat_id,db_file)
    id = retrieve_rules_list(db_file)[-1][0]

    my_rule= Rule(id,cat_id,name,description,bad_typo,good_typo)
    list_of_rules_obj.append(my_rule)

    


"""
function to modify a rule in the db (and in [list_of_rule_obj])
----

sqlite3.Connection con
Rule rule_object : the Rule object to modify
String new_name : new name of the rule
String new_description : new description of the rule
String new_bad_typo : the new String bad_typo of the Rule object // Rule("hello","world") --> Rule("hi","world")
String new_good_typo : the new String good_typo of the Rule object // Rule("hello","world") --> Rule("hello","guys")
----
----
author: Salvio Strazzante   
date: 08/03
"""
def modify_rule(rule_object,new_name,new_description,new_bad_typo,new_good_typo,new_cat_id,db_file='./application/data/DB/TypoChecker.db'):
    modify_db(rule_object.get_id(),new_name,new_description,new_bad_typo,new_good_typo,new_cat_id,db_file)

    rule_object.set_name(new_name)
    rule_object.set_description(new_description)
    rule_object.set_bad_typo(new_bad_typo)
    rule_object.set_good_typo(new_good_typo)
    rule_object.set_cat(new_cat_id)

    
   


"""
function to delete a rule in the db (and in [list_of_rule_obj])
----
Rule rule_object : the Rule object to delete
----
----
author: Salvio Strazzante   
date: 08/03
"""
def delete_rule(rule_object,db_file='./application/data/DB/TypoChecker.db'):

    remove_rule_from_db(rule_object.get_id(),db_file)

    index_to_del = list_of_rules_obj.index(rule_object)
    del rule_object #sinon garbage object
    del list_of_rules_obj[index_to_del]






"""
function to set the db rules into a list/list_of_rule_obj (to prevent sql calls each time we need a rule)
"""
def db_rules_to_list(db_file='./application/data/DB/TypoChecker.db'):
    for rule in retrieve_rules_list(db_file):
        my_rule = Rule(rule[0],rule[1],rule[2],rule[3],rule[4],rule[5])
        list_of_rules_obj.append(my_rule)



def print_all_object():
    for e in list_of_rules_obj:
        print('id : '+ e.get_id())
        print('bad : '+e.get_bad_typo())
        print('good : '+e.get_good_typo())
        print(" f"+e.get_cat())

list_of_rules_obj = []  










