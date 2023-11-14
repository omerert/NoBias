#################################################################################
#         FILE:
#           getTextFromWeb.py
#       AUTHOR:
#           Omer Erturk
#  DESCRIPTION:
#           
#           
# DEPENDENCIES:
#           Created with Python 3.12.0(Python version)
#           nltk, urllib.request, requests, bs4, wordnet
#################################################################################
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import urllib.request
import requests
from bs4 import BeautifulSoup
from nltk.corpus import wordnet as wn

#TODO Get link from user input
url = "https://abcnews.go.com/Politics/tens-thousands-expected-dc-pro-israel-rally-national/story?id=104861127"

#Gets source html

getRequest = requests.get(url)
htmlText = getRequest.text

#Using BS and strip_tags to get the text I want

soupText = BeautifulSoup(htmlText, 'html.parser')
wantedText = soupText.findAll("p")



with open('sentences.txt', 'w') as outFile:
    for para in wantedText:
        sentences = sent_tokenize(para.text.strip())
        for sent in sentences:
            
            outFile.write(sent)
        outFile.write("\n" + "=" * 80 + "\n")
        
            


    