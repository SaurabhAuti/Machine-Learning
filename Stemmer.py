# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 16:58:24 2023

@author: 91996
"""

import nltk
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords

paragraph = """" ChatGPT is an artificial intelligence chatbot developed by OpenAI and launched in November 2022. It is built on top of OpenAI's GPT-3 family of large language models and has been fine-tuned using both supervised and reinforcement learning techniques. """

sentences = nltk.sent_tokenize(paragraph)
sentences_2 = nltk.sent_tokenize(paragraph)
sentences_3 = nltk.sent_tokenize(paragraph)
stemmer = PorterStemmer()
stemmer_2 = LancasterStemmer()
stemmer_3 = SnowballStemmer('english')

for i in range (len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [stemmer.stem(word) for word in words if word not in set (stopwords.words('english'))]
    sentences[i] =' '.join(words)
 
for i in range (len(sentences_2)):
    words_2 = nltk.word_tokenize(sentences_2[i])
    words_2 = [stemmer_2.stem(word) for word in words_2 if word not in set (stopwords.words('english'))]
    sentences_2[i] =' '.join(words_2)
    
    
for i in range (len(sentences_3)):
    words_3 = nltk.word_tokenize(sentences_3[i])
    words_3 = [stemmer_3.stem(word) for word in words_3 if word not in set (stopwords.words('english'))]
    sentences_3[i] =' '.join(words_3)
    
    
