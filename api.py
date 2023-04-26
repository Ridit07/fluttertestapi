from flask import Flask, request, jsonify

app = Flask(__name__)


import pandas as pd
import numpy as np
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import math
import warnings
warnings.filterwarnings("ignore")

# Load the dataset
df = pd.read_csv("sbatting2.csv")
s='null'
pred='nulla'
def abc(balls,teamname,batsmanname):
    df1=df.loc[(df['fullName'] == batsmanname) & (df['away_team'] == teamname) ]
    X1 = df1[['ballsFaced']]
    y1 = df1['runs']
    X1_train,X1_test,y1_train,y1_test=train_test_split(X1,y1,test_size=0.1,random_state=0)
    linreg=LinearRegression()
    abc=linreg.fit(X1_train,y1_train)
    y1_pred=abc.predict(X1_test)
    Accuracy1=r2_score(y1_test,y1_pred)*100
    if(math.isnan (Accuracy1)):
        # print("cant say ")
        s='cant say'
    else:
        print(" Accuracy of the model is %.2f" %Accuracy1)
        s=str(Accuracy1)

    y2_pred=abc.predict([[balls]])
    pred=str(y2_pred)
    return s,pred



@app.route('/api', methods = ['GET'])
def returnascii():
    d = {}
    inputchr2 = str(request.args['teamname'])
    inputchr3 = str(request.args['batsmanname'])

    answer1,answer2=abc(25,inputchr2,inputchr3)


    





    d['accuracy'] = answer1
    d['runs'] = answer2
    return d

if __name__ =="__main__":
    app.run()
