"""----------------------Problem Statement----------------------"""
"Predictive Analysis using Breast Cancer Diagnostic dataset"



"""
    Attribute Information:

1) ID number
2) Diagnosis (M = malignant, B = benign)
-3-32.Ten real-valued features are computed for each cell nucleus:

a) radius (mean of distances from center to points on the perimeter)
b) texture (standard deviation of gray-scale values)
c) perimeter
d) area
e) smoothness (local variation in radius lengths)
f) compactness (perimeter^2 / area - 1.0)
g). concavity (severity of concave portions of the contour)
h). concave points (number of concave portions of the contour)
i). symmetry
j). fractal dimension ("coastline approximation" - 1)
The mean, standard error and "worst" or largest (mean of the three largest values) of these features were computed for each image, resulting in 30 features. For instance, field 3 is Mean Radius, field 13 is Radius SE, field 23 is Worst Radius

"""



" This model will use these Attributes to predict weather a tumor is Benign or Malignant "



import win32com.client
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

def say(text):
    speaker=win32com.client.Dispatch("SAPI.SpVoice")
    print(text)
    speaker.Speak(text)
def dataPreProcessing(df):
    df.drop('id', axis=1, inplace=True)
    df.drop('Unnamed: 32', axis=1, inplace=True)
    print(df.isnull().sum())
    return df

def classifier(model,dftrain,predictor,outcome):
    model.fit(dftrain[predictor],dftrain[outcome])

if __name__=='__main__':
    Data=pd.read_csv('BreastCancer.csv')
    Data_Cleaned=dataPreProcessing(Data)
    print(Data_Cleaned)
    dftrain,dftest=train_test_split(Data_Cleaned,test_size=0.3)
    predictor_var = ['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
                     'compactness_mean', 'concavity_mean', 'concave points_mean', 'symmetry_mean',
                     'fractal_dimension_mean', 'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
                     'compactness_se', 'concavity_se', 'concave points_se',
                     'symmetry_se', 'fractal_dimension_se', 'radius_worst', 'texture_worst', 'perimeter_worst',
                     'area_worst', 'smoothness_worst', 'compactness_worst', 'concavity_worst',
                     'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst']

    outcome_var = 'diagnosis'


    try:
        LR=LogisticRegression()
        classifier(LR,dftrain,predictor_var,outcome_var)
        pred=LR.predict(dftest[predictor_var])
        a=(100*accuracy_score(dftest[outcome_var],pred))




        model = DecisionTreeClassifier()
        classifier(model, dftrain, predictor_var, outcome_var)
        pred2=model.predict(dftest[predictor_var])
        b=(100*accuracy_score(dftest[outcome_var], pred2))



        KNN=KNeighborsClassifier()
        classifier(KNN, dftrain, predictor_var, outcome_var)
        pred3=model.predict(dftest[predictor_var])
        c=(100*accuracy_score(dftest[outcome_var], pred3))
    finally:
            print(f"{a} {b} {c}")
    if input("[A: Use premade dataset for prediction]\n[B: Use ur own data]\nenter ur choice:")=="A":
        pred_var=[[15.99, 10.38, 122.8, 1001, 0.1184, 0.2776, 0.3001, 0.1471,
               0.2419, 0.09, 1.1, 0.9053, 8.589, 153.4, 0.006399, 0.04904,
               0.05373, 0.01587, 0.03003, 0.006193, 25.38, 17.33, 184.6, 2019,
               0.1622, 0.6656, 0.7119, 0.3456, 0.5434, 0.1189]]
    else:
        pred_var=[]
        for i in range(0,30):
            pred_var.append(float(input(f'Input {predictor_var[i]}:')))
        pred_var=np.array(pred_var)
        pred_var=pred_var.reshape(1,30)
    print(pred_var)
    if a>b and a>c:
        out_var=LR.predict(pred_var)
        if out_var=='M':
            say('Sorry! But the Tumor is Malignant!')
        else:
            say('Hurray! The Tumor is Benign!')
    elif b>a and b>c:
        out_var=model.predict(pred_var)
        if out_var=='M':
            say('Sorry! But the Tumor is Malignant!')
        else:
            say('Hurray! The Tumor is Benign!')
    else:
        out_var = KNN.predict(pred_var)
        if out_var == "M":
            say("Sorry! But the Tumor is Malignant!")
        else:
            say("Hurray! The Tumor is Benign!")