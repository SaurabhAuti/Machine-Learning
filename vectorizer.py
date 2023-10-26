# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 14:36:29 2023

@author: 91996
"""

import nltk

paragraph = """I have three visions for India. In 3000 years of our history people from all over the world has
come and invaded us, captured our lands, conquered our lands, conquered our minds. From Alexander
onwards the Greeks, the Turks, the Mughals, the Portuguege, the British, the French, the Dutch, all of
them came and looted us, took over what was ours. Yet we have not done this to any other nation.
We have not conquered anyone. Who have not grabbed their land, their culture, their history and tried
to enforce our way of life on them. Why ? Because we respect the freedom of others. 
That is whymy first vision is that of freedom. It is this freedom that we must protect and nurture and build on.
My second vision for India is development. We are among the top five nations of the world. We
have ten percent growth rate in most area. Our achievements are being globally recognised today. Yet
we lack the self-confidence to see ourselves as a developed nation, reliant and self assured. Isn't it
incorrect? I have a third vision. India must stand up to the world. Because I believe that unless India
stands up to the world, no one will respect us. Only strength respects strength. We must be strong not
only as a military power but also as an economic power. Both must go hand in hand."""

import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

ps = PorterStemmer()
wordnet = WordNetLemmatizer()
sentences = nltk.sent_tokenize(paragraph)

corpus = []

for i in range(len(sentences)):
    review = re.sub('[^a-zA-z]',' ', sentences[i])
    review = review.lower()
    review = review.split()
    #review = [ps.stem(word) for word in words if word not in set (stopwords.words('english'))]
    review = [wordnet.lemmatize(word) for word in review if word not in set (stopwords.words('english'))]
    review =' '.join(review)
    corpus.append(review)
    
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
x = cv.fit_transform(corpus).toarray()

from sklearn.feature_extraction.text import TfidfVectorizer
cv1 = TfidfVectorizer()
x1 = cv1.fit_transform(corpus).toarray()


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    