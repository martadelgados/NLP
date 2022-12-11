#!/usr/bin/env python
# coding: utf-8

# # INFORMACIÓN NO ESTRUCTURADA

# In[1]:


import pandas as pd
pip install gensim
import gensim
from gensim.models import Word2Vec,KeyedVectors


# In[2]:


model = KeyedVectors.load_word2vec_format('SBW-vectors-300-min5.bin.gz',binary=True)


# In[ ]:


def guess():
    guesslist = pd.DataFrame(model.most_similar("", topn = topn), columns = ['words', 'similarity'])


# In[24]:


def guess(word, guessword, topn = 2000):
    guesslist = pd.DataFrame(model.most_similar("house", topn = topn), columns = ['words', 'similarity'])
    results = guesslist[guesslist['words'].str.contains(r'\b' + word + r'\b')]
    return results


# In[25]:


guess("techno", "house")


# In[10]:


user_guess = input("Enter a word to guess: ")
guess(user_guess, "house")


# In[18]:


guesslist = pd.DataFrame(model.most_similar("house", topn = 50), columns = ['words', 'similarity'])


# In[36]:


secret_word = "house"
def guess(secret_word, topn = 10000):
    guesslist = pd.DataFrame(model.most_similar(secret_word, topn = topn), columns = ['words', 'similarity'])
    return guesslist


# In[38]:


guesslist = guess(secret_word, 10000)


# In[39]:


user_guess = input("Please guess the secret word: ")
while user_guess != secret_word:
    print(guesslist[guesslist['words'].str.contains(r'\b' + user_guess + r'\b')])
    user_guess = input("Please guess the secret word again: ")
else:
    print("Correct!!!!!!!!!!")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




