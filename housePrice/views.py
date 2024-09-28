import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from  sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split
from sklearn import metrics
from django.shortcuts import render;
def home(request):
    return render(request, "home.html")
def predict(request):
    return render(request, "predict.html")
def result(request):
    data = pd.read_csv(r"E:\house-prediction\USA_Housing.csv")
    data =data.drop(['Address'],axis=1)
    X=data.drop('Price',axis=1)
    Y= data['Price']

    X_train,X_test,Y_train ,Y_test =train_test_split(X,Y,test_size=.30)
    model =LinearRegression()
    model.fit(X_train,Y_train)
    var1 = float(request.GET.get('n1', 0)) if request.GET.get('n1') else 0
    var2 = float(request.GET.get('n2', 0)) if request.GET.get('n2') else 0
    var3 = float(request.GET.get('n3', 0)) if request.GET.get('n3') else 0
    var4 = float(request.GET.get('n4', 0)) if request.GET.get('n4') else 0
    var5 = float(request.GET.get('n5', 0)) if request.GET.get('n5') else 0

    pred = model.predict(np.array([var1, var2, var3, var4, var5]).reshape(1,5))

    pred=round(pred[0])
    price="Predicted Price will be ₹"+str(pred)


    return render(request, "predict.html",{"result":price})
