from .rule_manager import *
from .manage_category_db import *


insecable = '\u00A0'


def remove_100_rule():
    for e in range(100):
        remove_rule_from_db(e+1,'test.db')
def create_rule(list_r):
    for e in list_r:
        x = e.split(' : ')
        print("add_rule('de "+x[0]+" à "+x[1]+"','','"+x[0]+"','"+x[1]+"')")

def add_init_category(db_file):
    add_category_to_db_and_id(0,'ALL',db_file)
    add_category_to_db('NO CATEGORY',db_file)
    add_category_to_db('Nombre',db_file)
    add_category_to_db('Acronyme',db_file)
    add_category_to_db('Abréviation',db_file)
    add_category_to_db('Grammaire',db_file)


    
    add_category_to_db('detectPonctuation',db_file)
    add_category_to_db('detectNombre',db_file)
    add_category_to_db('detectGuillemet',db_file)
    add_category_to_db('detectMajuscule',db_file)
    add_category_to_db('detectÉ,À,Ç',db_file)
    add_category_to_db('detectDoublons',db_file)


    add_category_to_db('detectLanguage',db_file)



def add_init_rules(db_file):

   
    add_rule('de ARD à Ardenne','','ARD','Ardenne',3,db_file)
    add_rule('de AFV  à Au fil de la Vesdre','','AFV','Au fil de la Vesdre',3,db_file)
    add_rule('de BBE à Brabant Est ','','BBE','Brabant Est',3,db_file)
    add_rule('de BRU à Brunehault ','','BRU','Brunehault',3,db_file)
    add_rule('de BAB à Bruxelles-Abbayes ','','BAB','Bruxelles-Abbayes',3,db_file)
    add_rule('de BAL à Bruxelles-Altitude ','','BAL','Bruxelles-Altitude',3,db_file)
    add_rule('de BXA à Bruxelles-Arcades ','','BXA','Bruxelles-Arcades',3,db_file)
    add_rule('de BXB à Bruxelles-Buda ','','BXB','Bruxelles-Buda',3,db_file)
    add_rule('de BWL à Bruxelles-Woluwe ','','BWL','Bruxelles-Woluwe',3,db_file)
    add_rule('de BZO à Bruxelles-Zénith Ouest ','','BZO','Bruxelles-Zénith Ouest',3,db_file)
    add_rule('de CHT à Chantoirs ','','CHT','Chantoirs',3,db_file)
    add_rule('de CHR à Charleroi ','','CHR','Charleroi',3,db_file)
    add_rule('de ESO à Entre-Sambre-Orneau ','','ESO','Entre-Sambre-Orneau',3,db_file)
    add_rule('de ESC à Escaut ','','ESC','Escaut',3,db_file)
    add_rule('de GML à Gaume-Lorraine ','','GML','Gaume-Lorraine',3,db_file)
    add_rule('de HOU à Hainaut-Ouest ','','HOU','Hainaut-Ouest',3,db_file)
    add_rule('de HED à Haine et Dendre ','','HED','Haine et Dendre',3,db_file)
    add_rule('de HSB à Hesbaye Est ','','HSB','Hesbaye Est',3,db_file)
    add_rule('de HHS à Hohe Seen ','','HHS','Hohe Seen',3,db_file)
    add_rule('de LSM à Les Sept Meuse ','','LSM','Les Sept Meuse',3,db_file)
    add_rule('de LTR à Les Trois Rivières ','','LTR','Les Trois Rivières',3,db_file)
    add_rule('de LBM à Liège Basse-Meuse ','','LBM','Liège Basse-Meuse',3,db_file)
    add_rule('de LRD à Liège-Rive droite ','','LRD','Liège-Rive droite',3,db_file)
    add_rule('de LRG à Liège-Rive gauche ','','LRG','Liège-Rive gauche',3,db_file)
    add_rule('de NAV à Namur-Vallées ','','NAV','Namur-Vallées',3,db_file)
    add_rule('de OET à Orne et Thyle ','','OET','Orne et Thyle',3,db_file)
    add_rule('de PDH à Pays de Herve ','','PDH','Pays de Herve',3,db_file)
    add_rule('de VMH à Val mosan-Huy ','','VMH','Val mosan-Huy',3,db_file)
    add_rule('de VML à Val mosan-Liège ','','VML','Val mosan-Liège',3,db_file)
    add_rule('de VDM à Vallée Dyle-Mazerine ','','VDM','Vallée Dyle-Mazerine',3,db_file)
    add_rule('de VBB à Vert Brabant ','','VBB','Vert Brabant',3,db_file)



    add_rule("de AnU à animateur d'unité",'','AnU',"animateur d'unité",3,db_file)
    add_rule("de EqU à équipier d'unité",'','EqU',"équipier d'unité",3,db_file)
    add_rule("de AnF à animateur fédéral",'','AnF',"animateur fédéral",3,db_file)
    add_rule("de AnR à animateur responsable",'','AnR',"animateur responsable",3,db_file)
    add_rule("de JANU à Journée annuelle des équipes d’unité",'','JANU',"Journée annuelle des équipes d’unité",3,db_file)


    add_rule('de Dr. à docteur','','Dr.','docteur',4,db_file)
    add_rule('de docteur à Dr.','','docteur','Dr.',4,db_file)



    add_rule('de MM. à messieur','','MM.','messieur',4,db_file)
    add_rule('de messieur à MM.','','messieur','MM.',4,db_file)
    add_rule('de M. à monsieur','','M.','monsieur',4,db_file)
    add_rule('de monsieur à M.','','monsieur','M.',4,db_file)

    add_rule('de Mmes à mesdames','','Mmes','mesdames',4,db_file)
    add_rule('de mesdames à Mmes','','mesdames','Mmes',4,db_file)

    add_rule('de Mme à madame','','Mme','madame',4,db_file)
    add_rule('de madame à Mme','','madame','Mme',4,db_file)

    add_rule('de NB à nota bene','','NB','nota bene',4,db_file)
    add_rule('de nota bene à NB','','nota bene','NB',4,db_file)
    add_rule('de PS à post scriptum','','PS','post scriptum',4,db_file)
    add_rule('de post scriptum à PS','','post scriptum','PS',4,db_file)
    add_rule('de € à euros','',insecable+'€','euros',4,db_file)
    add_rule('de euros à €','','euros',insecable+'€',4,db_file)
    add_rule('de p à page','','p.','page',4,db_file)
    add_rule('de page à p','','page','p.',4,db_file)
    add_rule('de pp à pages','','pp.','pages',4,db_file)
    add_rule('de pages à pp','','pages','pp.',4,db_file)
    add_rule('de confer à cf.','','confer','cf.',4,db_file)
    add_rule('de cf. à confer','','cf.','confer',4,db_file)



    add_rule('de et/ou à ou','','et/ou','ou',1,db_file)
    add_rule('de asbl à ASBL','','asbl','ASBL',1,db_file)
    add_rule('de gsm à GSM','','gsm','GSM',1,db_file)

    add_rule('de 0 à zéro','','0','zéro',2,db_file)
    add_rule('de 1 à un','','1','un',2,db_file)
    add_rule('de 2 à deux','','2','deux',2,db_file)
    add_rule('de 3 à trois','','3','trois',2,db_file)
    add_rule('de 4 à quatre','','4','quatre',2,db_file)
    add_rule('de 5 à cinq','','5','cinq',2,db_file)
    add_rule('de 6 à six','','6','six',2,db_file)
    add_rule('de 7 à sept','','7','sept',2,db_file)
    add_rule('de 8 à huit','','8','huit',2,db_file)
    add_rule('de 9 à neuf','','9','neuf',2,db_file)
    add_rule('de 10 à dix','','10','dix',2,db_file)
    add_rule('de onze à 11','','onze','11',2,db_file)
    add_rule('de douze à 12','','douze','12',2,db_file)
    add_rule('de treize à 13','','treize','13',2,db_file)
    add_rule('de quatorze à 14','','quatorze','14',2,db_file)
    add_rule('de quinze à 15','','quinze','15',2,db_file)
    add_rule('de seize à 16','','seize','16',2,db_file)

    add_rule('de maman à parent 2','','maman','parent 2',2,db_file)
    add_rule('de papa à parent 1','','papa','parent 1',2,db_file)







    add_rule('paranthèse gauche et 2 espace','',' ( ','(',5,db_file)
    add_rule('paranthèse gauche et before espace','',' (','(',5,db_file)
    add_rule('paranthèse gauche et after espace','','( ','(',5,db_file)


    add_rule('paranthèse droite et 2 espace','',' ) ',')',5,db_file)
    add_rule('paranthèse droite et before espace','',' )',')',5,db_file)
    add_rule('paranthèse droite et after espace','',') ',')',5,db_file)

    add_rule('virgule et 2 espace','',' , ',', ',5,db_file)  #. et ... aussi
    add_rule('virgule et before espace','',' ,',', ',5,db_file)

    add_rule("de trois petit points d'énumération à etc.",'','...',', etc.',5,db_file)

    add_rule('de espace ? à espace_insecable ?','',' ?',insecable +'? ',5,db_file)
    add_rule('de espace ! à espace_insecable ?','',' !',insecable +'! ',5,db_file)
    add_rule('de espace ; à espace_insecable ?','',' ;',insecable +'; ',5,db_file)
    add_rule('de espace : à espace_insecable ?','',' :',insecable +': ',5,db_file)
