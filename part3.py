# -*- coding: utf-8 -*-
"""

@author: wajahat
"""

import os
import string
import sys
from nltk.tokenize import RegexpTokenizer
from bs4 import BeautifulSoup
from bs4.element import Comment
from nltk.tokenize import word_tokenize
import nltk
from nltk.stem import SnowballStemmer
from string import punctuation
termids=dict()
termfile=open("termids.txt","r",errors='ignore')
indexfile=open("term_index.txt","r",errors='ignore')
if sys.argv[1]=='--term':
    
           
    word=sys.argv[2]
    #word="hello"
    token=[x.lower() for x in word if x.isalpha()]
    texts1=''.join(c for c in token if c  in string.printable)
    texts=''.join(c for c in texts1 if c not in punctuation)
    
    snowball_stemmer = SnowballStemmer('english')
    stemmed=snowball_stemmer.stem(texts)
    for x in termfile:
        lst=x.split("\t")
        termids.update({lst[1]:int(lst[0])})
    
    wordID=termids.get(stemmed+"\n",0)
    
    if(wordID != 0):
        for x in indexfile:
            lst1=x.split(" ")
            s=lst1[0]
            if(int(s)==wordID):
                print("Listing for term:",word)
                print("TERMID:",wordID)
                print("Number of documents containing term:",lst1[2])
                print("Term frequency in corpus:",lst1[1])
                break
           
    else:
        print("word does not exist!")
else:
    print("Wrong Command Format!")
    
termfile.close()