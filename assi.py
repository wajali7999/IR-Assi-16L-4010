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
termlist=[]

b=0;
#path= sys.argv[1]
path="D:\A.Fast sem 7\IR\corpus\corpus"

#def processFiles():
docID=open("docids.txt", "w",errors='ignore')
termID=open("termids.txt", "w",errors='ignore')
termDocPair = dict()
for file in os.listdir(path):
    b=b+1;
    if b is 5:
        break
    myfile = os.path.join(path, file)
    print(myfile);
    myfile=open(myfile,errors='ignore')
#myfile=open("D:\A.Fast sem 7\IR\corpus\corpus\clueweb12-0000wb-05-13668",'r')
    soup=BeautifulSoup(myfile, 'html.parser')    
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    
    if soup.find('body') is None:
        texts=""
    else: 
        texts = soup.find('body').text
         # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in texts.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        texts1 = '\n'.join(chunk for chunk in chunks if chunk)
      
        texts=''.join(c for c in texts1 if c not in punctuation)
        IDdoc=IDdoc+1       
        docID.write(str(IDdoc)+"\t"+file+"\n")

        tokenizer = RegexpTokenizer(r"\w+")  
        token = tokenizer.tokenize(texts) 
        tokens=[x.lower() for x in token]

        #print ("Total token count:",len(tokens))
        #print ("vocabulary size or token types:", len(set(tokens))) 
        
        st=open("D:\A.Fast sem 7\IR\corpus\stoplist.txt")
        stop=st.read()
        stoplist = list(stop.split("\n")) 
        
        for w in list(tokens):  
            if w in stoplist:
                tokens.remove(w)
#        if b is 1:
#            print(tokens)
        snowball_stemmer = SnowballStemmer('english')
        stemmed_word = [snowball_stemmer.stem(word) for word in tokens]
                
#        if b is 1:
#               print(stemmed_word)
        currentWordPos=0;
        
        for w in stemmed_word:
            #readtermID=termID.read()
            currentWordPos=currentWordPos+1
            if w not in termlist :
                termlist.append(w)
                IDterm=IDterm+1
                termID.write(str(IDterm) + "\t" + w + "\n")
                doclist=[]
                idDoc_Pos=str(IDdoc)+","+str(currentWordPos)
                doclist.append(idDoc_Pos)
                termDocPair.update( {IDterm : doclist} )
            else:
                #for tID,dID in termDocPair.items:
                idDoc_Pos=str(IDdoc)+","+str(currentWordPos)
                termDocPair[termlist.index(w)+1].append(idDoc_Pos)    
                
                
        
        for key in termDocPair:
            lst=termDocPair[key]
            set1=[]
            for i in lst:
                lst1=i.split(',')
                if lst1[0] not in set1:
                    set1.append(lst1[0])
               # print(lst1)
                
            print(str(key)+"  " + str(len(termDocPair[key]))+"  "+str(len(set1)) + "  " , termDocPair[key] )
        myfile.close()
#        stemmed_word.clear()
#        token.clear()
#        tokens.clear()
#        stoplist.clear()
docID.close()
termID.close()
        #print(tokens)
        #Sprint(token)
#        with open("output.txt", "a",errors='ignore') as ofile:
#            ofile.write(texts)
#        #print(texts)
#
#out=open("D:\A.Fast sem 7\IR\output.txt")
#tokenizer = RegexpTokenizer(r'\w+')
#file_txt= out.read()
#
##file_txt = out.decode('utf-8')
#token = tokenizer.tokenize(file_txt)  
#tokens=[x.lower() for x in token]
#print ("Total token count:",len(tokens))
#print ("vocabulary size or token types:", len(set(tokens))) 
#tokenCount = nltk.FreqDist(tokens)
#print (tokenCount)
#tokenCount.plot(20)  
#
#stop=open("D:\A.Fast sem 7\IR\corpus\stoplist.txt")
#stoplist=stop.read()