# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 22:32:32 2019

@author: wajahat
"""
#IR Assignment
import sys
import os
import requests
from nltk.tokenize import RegexpTokenizer
from bs4 import BeautifulSoup
from bs4.element import Comment
from nltk.tokenize import word_tokenize
import nltk
from nltk.stem import SnowballStemmer
from string import punctuation
IDdoc=0
IDterm=0;
termlist1=dict()

b=0;
path= sys.argv[1]
#path="D:\A.Fast sem 7\IR\corpus\corpus"

#def processFiles():
docID=open("docids.txt", "w",errors='ignore')
termID=open("termids.txt", "w",errors='ignore')
st=open("D:\A.Fast sem 7\IR\corpus\stoplist.txt")
stop=st.read()
stoplist = list(stop.split("\n")) 

filedict=dict()
for file in os.listdir(path):
#    b=b+1
#    if b is 5:
#        break
    myfile = os.path.join(path, file)
   # print(myfile);
    myfile=open(myfile,errors='ignore')
    s=os.path.splitext(file)
    
    if s[0]  in filedict:
        continue
    else:
        filedict.update( {s[0] : s[1]} )
        print(s[0])
        

    soup=BeautifulSoup(myfile, 'html.parser')    
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    
    if soup.find('body') is None:
        texts=""
    else: 
        texts = soup.find('body').text
        lines = (line.strip() for line in texts.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # removing blank lines and symbols
        texts1 = '\n'.join(chunk for chunk in chunks if chunk)
        texts=''.join(c for c in texts1 if c not in punctuation)

        IDdoc=IDdoc+1       
        docID.write(str(IDdoc)+"\t"+file+"\n")

        tokenizer = RegexpTokenizer(r"\w+")  
        token = tokenizer.tokenize(texts) 
        tokens=[x.lower() for x in token if x.isalpha()]

        #print ("Total token count:",len(tokens))
        #print ("vocabulary size or token types:", len(set(tokens))) 

        
        for w in list(tokens):  
            if w in stoplist:
                tokens.remove(w)

        snowball_stemmer = SnowballStemmer('english')
        stemmed_word = [snowball_stemmer.stem(word) for word in tokens]
                

        currentWordPos=0;
        
        for w in stemmed_word:
            if w not in termlist1 :
                IDterm=IDterm+1
                termlist1.update( {w : IDterm} )
                termID.write(str(IDterm) + "\t" + w + "\n")
              
    
                
        
        stemmed_word.clear()
        token.clear()
        tokens.clear()
        stoplist.clear()
        myfile.close()
   
docID.close()
termID.close()
