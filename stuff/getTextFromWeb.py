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
# from app import input_data
# print(input_data)
#TODO Get link from user input
url = "https://www.reuters.com/investigates/special-report/tesla-insurance/"

#Gets source html

getRequest = requests.get(url)
htmlText = getRequest.text

#Using BS and strip_tags to get the text I want

soupText = BeautifulSoup(htmlText, 'html.parser')
wantedText = soupText.findAll("p")


def pasteText(list):
    for para in wantedText:
        sentences = sent_tokenize(para.text.strip())
        for sent in sentences:
            list.append(sent + "\n")
        list.append("*" * 500)
            
           

    
        
            


    