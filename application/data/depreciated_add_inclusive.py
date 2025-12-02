import spacy

#ECRITURE INCLUSIVE

"""

Nous tenons néanmoins à représenter le masculin et le féminin de manière égale dans nos
publications. C’est pourquoi nous avons choisi d’appliquer ces trois règles de base :
1. Mettre les deux termes dans l’introduction (masculin et féminin) : formateurs et
formatrices.
2. Lorsqu'on utilise un terme épicène, comme architecte, il faut signaler les deux genres
dans l’adjectif qualificatif : les architectes sont content-e-s.
3. Se concentrer en priorité sur les parties clés d’un texte (titre – intro – chapeau –
conclusion)."""



nlp = spacy.load("fr_core_news_sm")
doc = nlp(text)
for sent in doc.sents:
        for token in sent:
            if token.ent_type==masc or fem and not plur:
                  add -e add trices
            if plur:
                  add -e-s
                  