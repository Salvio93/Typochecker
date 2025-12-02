#import spacy
from .rule_manager import *
from .document_manager import *
from .manage_document_rule_db import *
from .detect_correct import *

from .create_structure_db import *
from .create_init_rule import *

def main():
    try :
        create_all()
        add_init_rules() 
        add_init_category()

        get_file_from_db()
    finally:
        #create list_of_rule_obj, from rule table

        db_rules_to_list()
        #./application/data/DB/TypoChecker.db'

        #create it in the db or retireieve it

        print_all_object()
        print_rule_db()
        print_docu_db()
        print_docu_rule_db()
        print_categoty_db()


#-----------------WORK IN PROGRESS-------------
#to detect:

#Tiret et trait d’union
#ALT+0183 point mediant
        
        
"""
Pour obtenir le É : Alt + 144
Pour obtenir le È : Alt + 212
Pour obtenir le Ç : Alt + 128
Pour obtenir le À : Alt Gr + è + Maj + A
Ç (Alt+0199)
Le caractère “e dans l’o” minuscule œ (Alt+0156) et majuscule Œ (Alt+0140)
Le caractère “e dans l’a” minuscule æ (Alt+0230) et majuscule Æ (Alt+0198)

"""

#-----ajouter bouton pour copier E majuscule... ?
#------Outils de recherche de mots dans le texte?
#----filtre par categuories d'errur 
#------apply error better interface/-
#----ecran chargement

#-------detect pdf/-


        

#PAGE 7 VOIR
"""Quelques remarques d’utilisation :
 « Fais circuler l’information dans tes unités » et non pas « dans ton groupe d’unités ».
En effet, le cadre fédéral est un animateur fédéral ou équipier fédéral d’unités, et non
pas d’un groupe.

On dira donc "animateur fédéral d’unités" et non pas "animateur fédéral de groupe
d’unités".
On parle des “cadres fédéraux chargés de ton unité”, ou mieux encore, “l’équipe
fédérale chargée du soutien de ton unité”. On ne dit pas “cadres de ton groupe d’unités”.
Quand on veut parler des cadres fédéraux, on n’oubliera pas l’adjectif "fédéral". Si on
parle de cadres (sans préciser local ou fédéral), cela comprend les cadres locaux
(équipes d’unités) et les cadres fédéraux.
On n’écrit pas « Contacte la fédération », mais « Contacte le 21 (sans guillemets), siège
de la fédération. »"""





#On utilise les crochets et les points de suspension lorsqu’on supprime un passage dans une citation ou un extrait de livre. Exemple : « Les scouts étaient nombreux […] ; ils se promenaient dans les bois. »


#add_rule('nos principes fondamentaux.', 'nos fondamentaux')
#Loi et Promesse devient l'adhésion aux valeurs.
#Le 8e élément de la méthode scoute s'intitule l'engagement dans la communauté.
#L’élément de la méthode Relation devient La relation éducative.





#DICTIONNAIRE

"""Akela, Bagheera, Baloo, Bandar-Log, Buldéo, Chil, Clan Seonee, Darzee, Chuchundra, Dholes,
Ferao, Frère Gris, Hathi, Jacala, Kaa, Kala-Nag, Ko, Mang, Messua, Mor, Mowgli, Nag et
Nagaina, Nathoo, Père Loup, Petit Toomaï, Peuple des Rochers, Phao, Raksha, Rama, Rikki-
Tikki-Tavi, Sahi, Shere-Kan, Tabaqui, Tha, Thuu, Won-Tolla.

les cinq contrées de Nyeri
la vallée du Yangin
l’ile Fajro
le hameau de Kalayo
la forêt de Tân
la source du Wuta

une baladine
une louvette
une éclaireuse
une pionnière
une routière


"""
#p12


#p8-9-10