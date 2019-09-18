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

if sys.argv[1]=='--term':
        
        word=sys.argv[2]
        token=[x.lower() for x in word if x.isalpha()]
        texts1=''.join(c for c in token if c  in string.printable)
        texts=''.join(c for c in texts1 if c not in punctuation)
        
        snowball_stemmer = SnowballStemmer('english')
        #stemmed_word = [snowball_stemmer.stem(w) for w in word]
        print(snowball_stemmer.stem(texts))
else:
    print("Wrong Command Format!")