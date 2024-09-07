"""-----------Problem Statement-----------"""
"Creating a Crop Recommendation system using Cultivation Dataset"
"""
    Dataset:
1) N- Nitrogen Level in the soil (Range:0-140)
2) P- Phosphorus level in soil (Range:5-145)
3) K- Potassium level in soil (Range:5-205)
4) Temperature (Range:8.8-43.7)
5) Humidity (Range:14.26-99.99)
6) pH (Range:3.5-9.9)
7) Rainfall (Range:20.211-298.5601)

"""


"This model aims at analysing the dataset and predict a suitable crop from the list of crops using machine learning model"


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from win32com.client import Dispatch
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

def say(text):
  speaker=Dispatch("SAPI.SpVoice")
  print(text)
  speaker.Speak(text)
say("Hello")

"""Data Reading and Splitting"""

Data=pd.read_csv("Crop_recommendation.csv")

print(Data)

cols=Data.iloc[0:0,:8]

labels=Data['label'].unique()
len=[*range(0,22)]
print(len)

xtrain,xtest,ytrain,ytest=train_test_split(Data.iloc[:,:7],Data['label'],test_size=0.3)
ytrain.shape

"""Model Building"""

def print_score(classifier,xtest,ytest):
  pred=classifier.predict(xtest)
  score1=100*accuracy_score(ytest,pred)
  print(f'Accuracy Score: {score1}')
  return score1

"""Logistic Regression"""

class LoR:
  model=LogisticRegression()
  model.fit(xtrain,ytrain)

score1=print_score(LoR.model,xtest,ytest)

"""KNeighborsClassifier"""

class KNN:
  model=KNeighborsClassifier()
  model.fit(xtrain,ytrain)

score2=print_score(KNN.model,xtest,ytest)

"""Naive Bayes Classifier"""
class NB:
  model=GaussianNB()
  model.fit(xtrain,ytrain)
score3=print_score(NB.model,xtest,ytest)

"""Decision Tree Classifier"""

class DTC:
  model=DecisionTreeClassifier()
  model.fit(xtrain,ytrain)
score4=print_score(DTC.model,xtest,ytest)
predt=[]
pred_var=[]
while True:
  for i in range(0,7,):
    predt.append(int(input(f'Input {cols} val {i}:')))
  pred_var.append(predt)
  if max(score1,score2,score3,score4)==score1:
    pred=LoR.model.predict(pred_var)
    say(f'{pred} is the perfect crop.')
  if max(score1,score2,score3,score4)==score2:
    pred=KNN.model.predict(pred_var)
    say(f'{pred} is the perfect crop.')
  if max(score1,score2,score3,score4)==score3:
    pred=NB.model.predict(pred_var)
    say(f'{pred} is the perfect crop.')
  if max(score1,score2,score3,score4)==score4:
    pred=DTC.model.predict(pred_var)
    say(f'{pred} is the perfect crop.')
  break