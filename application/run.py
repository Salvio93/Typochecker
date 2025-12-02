from data.rule_manager import *
from data.document_manager import *
from data.manage_document_rule_db import *
from data.create_structure_db import *
from data.main import *

from ui import views
from ui.views import app
import os
# setup objects
sessions_data = {}
views.get_session_data

# run
if __name__ == '__main__':
    """
    if os.path.exists('./application/data/DB/TypoChecker.db'):
        os.remove('./application/data/DB/TypoChecker.db')
        create_all('./application/data/DB/TypoChecker.db')
        add_init_category('./application/data/DB/TypoChecker.db')
        add_init_rules('./application/data/DB/TypoChecker.db') 
    """

        #create list_of_rule_obj, from rule table
    db_rules_to_list('./application/data/DB/TypoChecker.db')

    print("rules loaded")
    
    # run app
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.debug = True
    app.run(host='0.0.0.0', port=5000)