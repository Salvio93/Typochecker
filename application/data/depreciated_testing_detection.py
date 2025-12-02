from main import *
from application.data.depreciated_get_set_docx import *
from application.data.depreciated_pdf_highlighting import*

import os
db_rules_to_list()


def testing_index(texte,document_id):
    remove_docu_rule_db_by_document_id(document_id)
    detect_bad_paragraph(texte,document_id)
    print_docu_rule_db()
    liste_of_docu_rule = retrieve_docu_rule_list_by_document_id(document_id)
    for rule in liste_of_docu_rule:
        print(retrieve_rules_by_id(rule[2]))
    ls0 = liste_of_docu_rule
    ls=[]
    for tupl in ls0:
        ls.append(list(tupl))
    for appliable_rule in liste_of_docu_rule:
        texte = getText('./test.docx')
        if appliable_rule[-1]!=1:
            texte =correct_bad_paragraph(texte,appliable_rule[0])

            diff_len = len(retrieve_rules_by_id(appliable_rule[2])[4]) - len(retrieve_rules_by_id(appliable_rule[2])[3])
            index =liste_of_docu_rule.index(appliable_rule)
         
            try:
                ls[index+1][-2]+=diff_len
            except:
                print('')
            try:

                assert(ls[index+1][-2] ==liste_of_docu_rule[index+1][-2]+diff_len)
            except:
                try:
                    print(ls[index+1][-2] ,' ----',liste_of_docu_rule[index+1][-2] )
                except:
                    print('')
            setText(texte,'./test.docx')
        else:
            set_high('./test.docx',rule[0])

    
    
filename_docx= './test.docx'
filename_pdf = './test.pdf'
filename_pdf_tmp = filename_pdf

text =getText(filename_docx)

remove_docu_rule_db_by_document_id(1)
detect_bad_paragraph(text,1)
list_of_docu_rule= retrieve_docu_rule_list_by_document_id(1)

last_correction = None
list_correction = [i[0] if i[-1]==0 else last_correction for i in list_of_docu_rule]

for correction in list_correction:
    if correction!= None:
        last_correction = correction

for e in list_of_docu_rule:
    #list_of_rules_obj
    texte =getText(filename_docx)
    if (e[-1]==0):
        bad_typo =retrieve_rules_by_id(e[2])[3]

        if e[0] != last_correction:
            if filename_pdf_tmp ==filename_pdf:
                print('---1'+filename_pdf_tmp)
                pdf_set_highlight(bad_typo,filename_pdf,filename_pdf.split('.pdf')[0]+'_tmp.pdf') 

                filename_pdf_tmp = filename_pdf.split('.pdf')[0]+'_tmp.pdf'

            else:      
                if filename_pdf_tmp == filename_pdf.split('.pdf')[0]+'_tmp.pdf':
                    print('---2'+filename_pdf_tmp)

                    pdf_set_highlight(bad_typo,filename_pdf_tmp,filename_pdf.split('.pdf')[0]+'_tmp1.pdf') 
                    filename_pdf_tmp = filename_pdf.split('.pdf')[0]+'_tmp1.pdf'
                else:
                    if filename_pdf_tmp == filename_pdf.split('.pdf')[0]+'_tmp1.pdf':
                        print('---3'+filename_pdf_tmp)

                        pdf_set_highlight(bad_typo,filename_pdf_tmp,filename_pdf.split('.pdf')[0]+'_tmp.pdf') 
                        filename_pdf_tmp = filename_pdf.split('.pdf')[0]+'_tmp.pdf'

        else:
            print('---4')

            pdf_set_highlight(bad_typo,filename_pdf_tmp,filename_pdf.split('.pdf')[0]+'_highlight.pdf')
            


            if os.path.exists(filename_pdf.split('.pdf')[0]+'_tmp.pdf'):
                os.remove(filename_pdf.split('.pdf')[0]+'_tmp.pdf')
            if os.path.exists(filename_pdf.split('.pdf')[0]+'_tmp1.pdf'):
                os.remove(filename_pdf.split('.pdf')[0]+'_tmp1.pdf')

        texte=correct_bad_paragraph(texte,e[0])
        setText(texte,filename_docx)
      
