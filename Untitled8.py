#!/usr/bin/env python
# coding: utf-8

# # INFORMACIÓN NO ESTRUCTURADA

import streamlit as st
st.title('Guess The Word')

import pandas as pd
from gensim.models import Word2Vec,KeyedVectors
import warnings
warnings.filterwarnings('ignore')


guesslist = "/data/guesslist_example"

secret_word = "madre"

# Función que solo muestra el df si no está vacío
def is_empty(df):
    if results.empty == False:
        display(df)
    else:
        print("Esta palabra no ha sido muy acertada...")

# Función que indica pistas para adivinar la palabra
def is_pista(pista, secret_word, guesslist):
    if pista == "pista1":
        print("La primera letra de la palabra es: " + secret_word[0])
    if pista == "pista2":
        print("La longitud de la palabra es: " + str(len(secret_word)))
    if pista == "pista3":
        print("La palabra más similar es " + str(model.most_similar(secret_word, topn = 1)))


# In[20]:


user_guess = input("Intenta adivinar la palabra: ")
results = pd.DataFrame()
while user_guess != secret_word:
    is_pista(user_guess, secret_word, guesslist)
    results = results.append(guesslist[guesslist['words'].str.contains(r'\b' + user_guess + r'\b')])
    results = results.sort_values('similarity', ascending = False)
    results = results.drop_duplicates()
    is_empty(results)
    user_guess = input("Intenta adivinar la palabra: ")
else:
    print("Muy biennn!!!!")


# In[21]:


guesslist.head(50)


# In[24]:


guesslist.to_parquet("guesslist_example")





