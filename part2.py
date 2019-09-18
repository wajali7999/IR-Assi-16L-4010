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
import string
IDdoc=0
IDterm=0;
termlist1=dict()

b=0;
path= sys.argv[1]
#path="D:\A.Fast sem 7\IR\corpus\corpus"

#def processFiles():
#docID=open("docids.txt", "w",errors='ignore')
#termID=open("termids.txt", "w",errors='ignore')
#termIndex=open("term_index.txt","w+",errors='ignore')
encodedindex=open("term_index.txt","w+",errors='ignore')
termDocPair = dict()
filedict=dict()
st=open("D:\A.Fast sem 7\IR\corpus\stoplist.txt")
stop=st.read()
stoplist = list(stop.split("\n")) 
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
        texts2 = '\n'.join(chunk for chunk in chunks if chunk)
        texts1=''.join(c for c in texts2 if c  in string.printable)
        texts=''.join(c for c in texts1 if c not in punctuation)
        #texts=''.join(c for c in texts2 if c.isalpha())
        IDdoc=IDdoc+1       
        #docID.write(str(IDdoc)+"\t"+file+"\n")

        tokenizer = RegexpTokenizer(r"\w+")  
        token = tokenizer.tokenize(texts) 
        tokens=[x.lower() for x in token if x.isalpha()]

        #print ("Total token count:",len(tokens))
        #print ("vocabulary size or token types:", len(set(tokens))) 
        

        
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
            if w not in termlist1 :
                IDterm=IDterm+1
                termlist1.update( {w : IDterm} )
                #termID.write(str(IDterm) + "\t" + w + "\n")
                doclist=[]
                idDoc_Pos=str(IDdoc)+","+str(currentWordPos)
                doclist.append(idDoc_Pos)
                termDocPair.update( {IDterm : doclist} )
            else:
                #for tID,dID in termDocPair.items:
                idDoc_Pos=str(IDdoc)+","+str(currentWordPos)
                termDocPair[termlist1[w]].append(idDoc_Pos)    
                
        
        stemmed_word.clear()
        token.clear()
        tokens.clear()
        stoplist.clear()
        myfile.close()
        
encoded=dict()
for key in termDocPair:
    lst=termDocPair[key]
    ch=0
    set1=[]
#    pr=lst[0].split(',')
#    prev=pr[0]
    doclistNew=[]
    for i in lst:
        lst1=i.split(',')
        if lst1[0] not in set1:
            set1.append(lst1[0])
            
        if ch == 0:
            doclistNew.append(termDocPair[key][0])
            ch=ch+1
            prev=int(lst1[0])
            prevpos=int(lst1[1])
            
        else:
            curr=int(lst1[0])
            currpos=int(lst1[1])
            enc=curr-prev
            if enc==0:
                idDoc_Pos=str(enc)+","+str(currpos-prevpos)
            else: 
                idDoc_Pos=str(enc)+","+str(lst1[1])
            doclistNew.append(idDoc_Pos)
            prev=curr
            prevpos=currpos
        #prev=lst1[0]
       # print(lst1)
    encoded.update({key:doclistNew})
    indexenc=str(key)+" " + str(len(encoded[key]))+" "+str(len(set1)) + " " + ' '.join(encoded[key]) 
    encodedindex.write(indexenc+"\n")
   # print(str(key)+" " + str(len(termDocPair[key]))+" "+str(len(set1)) + " " + ' '.join(termDocPair[key]) )
   # index=str(key)+" " + str(len(termDocPair[key]))+" "+str(len(set1)) + " " + ' '.join(termDocPair[key]) 
  #  termIndex.write(index+"\n")
       
    

