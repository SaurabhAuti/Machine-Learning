import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = pd.read_csv(r'C:\Users\91996\Desktop\python\cars1.csv')
x=dataset.iloc[:, :-1].values
y=dataset.iloc[:, 3].values
from sklearn.impute import SimpleImputer 
imputer = SimpleImputer() 
imputer = imputer.fit(x[:,1:3]) 
x[:, 1:3] = imputer.transform(x[:,1:3])
from sklearn.preprocessing import LabelEncoder
labelencoder_x= LabelEncoder()
labelencoder_x.fit_transform(x[:,0])
