# TypoChecker
 Outil de relecture typographique intelligente pour une ASBL

# Prérequis
installer python 3.12 https://www.python.org/downloads/ \
installer git         https://git-scm.com/downloads

# Installation
```bash
git clone https://github.com/Salvio93/TypoChecker
cd TypoChecker
pip install -r .\requirements.txt
```

## Lancer l'application
### 1. lancer dans un terminal
```bash
python application/run.py
```

### 2. accéder à l'application
Un ordinateur sur le réseau doit lancer la commande d'en haut, et ensuite toutes les autres personnes sur le réseau auront accès à l'application en allant sur l'IP de l'ordinateur qui host l'application.
Donc par exemple si l'IP de l'odinateur qui host est 123.456.789.10 ,il faudra écrire http://123.456.789.10:5000 dans le navigateur.

Evidemment, si l'odinateur qui host veut accéder à l'appli plus simplement, il lui suffira d'écrire http://127.0.0.1:5000

## Structure de la db
![Alt text](doc/db.png?raw=true "Title")

## La spécification des fonctions devra suivre la charte ci-dessous:

```
"""
description
----
param: 
----
return:
----
author:
date:
"""
```
