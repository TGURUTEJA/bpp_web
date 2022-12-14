from http.client import HTTPResponse
from django.shortcuts import render
import pickle
import pandas as pd

# Create your views here.
def home(request):
    global location
    data=pd.read_csv("Cleaned_data.csv")

    location=sorted(data['location'].unique())
    return render(request,'index.html',{"locations":location})
def prediction(request):
    data=pd.read_csv("Cleaned_data.csv")
    location=sorted(data['location'].unique())
    pipe=pickle.load(open('RidgModel.pkl','rb'))
    loc=request.GET['loc']
    sqft=request.GET['total_sqrt']
    bath=request.GET['bath']
    bhk=request.GET['bhk']
    input=pd.DataFrame([[loc,sqft,bath,bhk]],columns=['location','total_sqft','bath','bhk'])
    prediction=pipe.predict(input)[0]*1e5
    return render(request,'index.html',{"result":prediction,"locations":location})