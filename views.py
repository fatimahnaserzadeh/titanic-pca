from flask import Flask,render_template,url_for,request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

def kl_divergence(p,q):
    return np.sum(np.where(np.logical_and(p!=0,q!=0),p*np.log(p/q),0))

data= pd.read_csv('data/titanic.csv')
data = data.dropna(subset=['Age'])

count,devision = np.histogram(data.Age,bins = 8)
data_norm = norm.rvs(size = len(data.Age),loc = data.Age.mean(),scale = data.Age.std())
count2,devision2 = np.histogram(data_norm,bins=8)


kl_divergence(count,count2)
plt.title('KL')
plt.plot(count,c = 'blue')
plt.plot(count2,c='red')
#accoding to the plot distribution of Age is not normal

plt.savefig("./static/Figure_1.png")

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/titanic')
def titanic():
    return render_template('titanic.html')










if __name__=='__main__':
    app.run(debug=True)