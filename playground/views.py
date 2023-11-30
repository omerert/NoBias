from django.shortcuts import render
from django.http import HttpResponse
from stuff.getTextFromWeb import pasteText

# Create your views here.
# Takes request and returns responce
listOfText = []
pasteText(listOfText)
def say_hello(request):
    return HttpResponse(listOfText)