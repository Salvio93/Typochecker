import fitz
from pprint import pprint


def pdf_set_highlight(texte,filename_src,filename_dst):
    doc = fitz.open(filename_src)
    for page in range(doc.page_count):
        rl = doc[page].search_for(texte)

        doc[page].add_highlight_annot(rl)

    doc.ez_save(filename_dst)

#pdf_set_highlight('test','./test.pdf','./test_highlight.pdf')
#pdf_set_highlight('famille','./test_highlight.pdf','./test_highlight2.pdf')