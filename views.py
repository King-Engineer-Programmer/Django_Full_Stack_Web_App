
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Twitter_User_Id
import random
import spacy
from spacy import displacy
from .models import Twitter_User_Idddz
from .models import graph_plotly
import pandas as pd 
from plotly.offline import plot
import plotly.express as px 
import pyttsx3
engine = pyttsx3.init()
#from pyttsx3 import *
from gtts import gTTS
import time
from home.sentiments import get_sentiment
from newsapi import NewsApiClient
from dotenv import load_dotenv
load_dotenv
import nltk
from nltk.corpus import wordnet
#import pypiwin32
import speech_recognition as sr


# Create your views here.





class ChatbotClass:

    

   

    def one(self):

        # say method on the engine that passing input text to be spoken
      
        engine.say('Hello everyone, I am an AI chatbot and I will be helping with the Tweet Sentiment Analysis. In this project we will anaylze tweets and extract relevant data for Segmenting Customer using various techniques, I hope you enjoy!')
        engine.runAndWait()
  
       
        

       
        






def chatbot(request):

    varone=ChatbotClass() # Instatiating the class
    engine = pyttsx3.init() # Creating a vraible for initializing
    varone.one() # calling the first function in the class for the voice

    return render(request, 'chatbot.html')













def suggested_followers(request):



    
    # Querying the Database via Django API
    data3=Twitter_User_Idddz.objects.all().filter(Username_Username=request.user.username).order_by('-Date_Time').values()[:1] 

  

    
    
    query_value=''

    for values in data3:
        new_values=values
        for k, v in new_values.items():
            if k=='Subject_Field':
                query_value=v
                for i, j in new_values.items():
                    if i=='Sentiment_Score' and j==1:
                        ss=1
                       
                    elif i== 'Sentiment_Score' and j==0:
                        ss=0
        
   
    data3=Twitter_User_Idddz.objects.all().exclude(Username_Username=request.user.username).filter(Subject_Field=query_value,Sentiment_Score=ss).order_by('-Date_Time').values()
 

    return render(request, 'followers.html', {'data3':data3} )






def home(request):
    user_data_id=request.user.id
    data= Twitter_User_Idddz.objects.exclude(id=request.user.id)[:5]
  
    return render(request, 'home.html', {'data':data})
  
  
def data(request):
    #import pyttsx3
   
data2= Twitter_User_Idddz.objects.all().order_by('-Date_Time').values()[:1]
    
    return render (request, 'data.html', {'data2':data2} )

   


def tweet_analyzer(request):
    import spacy


    if request.method =='POST':
        # import random
        
       
        Tweet=request.POST['text']
        user_id=request.user
        Sentiment_Score=get_sentiment(Tweet)[0][0] 
        nlp=spacy.load("en_core_web_sm")
        doc=nlp(Tweet)
        sentences=list(doc.sents)
        sentence=(sentences[0])

        pronoun_array=[]
        noun_array=[]
        aux_array=[]
        verb_array=[]
        adjective_array=[]
        subject_array=[]

        for token in sentence:
    
            if token.pos_=='NOUN':
             noun_array.append(token.pos_)
             subject_array.append(token.text)

            elif token.pos_=='PRON':
             pronoun_array.append(token.pos_)
             
       
            elif token.pos_=='AUX':
             aux_array.append(token.pos_)

            elif token.pos_=='VERB':
             verb_array.append(token.pos_) 
            
            elif token.pos_=='ADJ':
             adjective_array.append(token.pos)

        if len(noun_array)>0:
            noun=len(noun_array)
        else:
            noun=0
            # print(noun) 

    
        if len(pronoun_array)>0:
            pronoun=len(pronoun_array)
        else:
            pronoun=0
            # print(pronoun) 

    
        if len(verb_array)>0:
            verb=len(verb_array)
        else:
            verb=0
            # print(verb) 

    
        if len(adjective_array)>0:
            adjective=len(adjective_array)
        else:
            adjective=0
            # print(adjective) 

        if len(aux_array)>0:
            aux_verbs=len(aux_array)
        else:
            aux_verbs=0
            # print(aux_verbs) 

        if len(subject_array)>0:
            subject=subject_array[0]
        else:
            subject='None'
            # print(subject) 


        Sentiment_Score=get_sentiment(Tweet)[0][0]
        z=Twitter_User_Idddz.objects.create(Tweet=Tweet,User_Id=user_id,Subject_Field=subject,Noun=noun,Pronoun=pronoun,Auxilary_Verbs=aux_verbs,Verb=verb,Sentiment_Score=Sentiment_Score,Customer_Score=1,Adjective=adjective,Username_Username=request.user.username)
        z.save()
     

        print(Sentiment_Score)
        return redirect('data')



    else:

      
      
        return render (request, 'tweetpage.html')


def data_graphs(request):

       return render (request, 'data2.html')

   

def api_call(request):
    

    from nltk.corpus import wordnet
    data2= Twitter_User_Idddz.objects.all().order_by('-Date_Time').values()[:1]
    
    
           
    synonyms = []
    antonyms = []
   
    for values in data2:
        new_values=values
        for k, v in new_values.items():
            if k=='Subject_Field' and v !='None':
                query_value=v
            elif k=='Subject_Field' and v=='None': 

                for i, j in new_values.items():
                    if i=='Sentiment_Score' and j==1:
                        query_value='happy'     # For no value and Positive Score - search a happy subject
                        for syn in wordnet.synsets(query_value):
                            for l in syn.lemmas():
                                synonyms.append(l.name())
                                if len(synonyms) > 0:
                                    query_value=synonyms[0]
                       
                    elif i== 'Sentiment_Score' and j==0:
                        query_value='sad'    # For no value and Negative Score - search something that is happy also
                        for syn in wordnet.synsets(query_value):
                            for l in syn.lemmas():
                                antonyms.append(l.name())
                                if len(antonyms) > 0:
                                    query_value=antonyms[0]  # Becomes happy here

          

   


    newsapi = NewsApiClient(api_key ='xxxxxxxxxxxxxxxxxxxxxxxxx')
    top = newsapi.get_everything(q=query_value,  sources ='techcrunch')
  
    l = top['articles']
    desc =[]
    news =[]
    img =[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        mylist = zip(news, desc, img)
  
   



    return render (request, 'api.html', {"mylist":mylist} )



