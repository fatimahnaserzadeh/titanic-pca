from flask import Flask,render_template,url_for,request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import normalize
import  matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/titanic')
def titanic():
    return render_template('titanic.html')






def preparing_data():
    titanic = sns.load_dataset('titanic')
    titanic = titanic.drop(['sex','embarked','class','who','adult_male','deck','embark_town','alive','alone'],axis = 1)
    titanic['age'] = titanic['age'].fillna(method = 'ffill')

    for label in ['pclass','age','sibsp','parch','fare']:
        titanic[label] = LabelEncoder().fit_transform(titanic[label])
    
    labels = titanic['survived']
    features = titanic.drop(['survived'],axis=1)
    model = PCA(n_components=3)
    model.fit(features)
    X_3D = model.transform(features)
    data = [X_3D,labels]
    return data




def display_data():
    data = preparing_data()
    labels = data[1]
    X_3D = data[0]
    live_x,live_y,live_z = X_3D[labels==1].T
    dead_x,dead_y,dead_z = X_3D[labels==0].T

    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111,projection='3d')

    ax.scatter(live_x,live_y,live_z,c='r',
    label='Casualties',marker='o')
    ax.scatter(dead_x,dead_y,dead_z,c='b',label='Survivors',marker='^')
    ax.legend()

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.savefig("./static/Figure_1.png")






display_data()



if __name__=='__main__':
    app.run(debug=True)