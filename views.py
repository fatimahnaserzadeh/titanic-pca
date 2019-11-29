from flask import Flask,render_template
from prettytable import PrettyTable
app = Flask(__name__)

def to_html_converter(path):
    path = 'data/{}.csv'.format(path)
    csv_file = open(path,'r')
    csv_file = csv_file.readlines()

    #creates a list of 6 first items of csv_file
    line = [] 
    for i in range(6):
        line.append(csv_file[i])
    #splits items at ','
    for i in range(len(line)):
        line[i] = line[i].split(',')
    
    x = PrettyTable()
    column_names = []
    for i in range(len(line[0])):
        column_names.append(line[0][i])
    # column_names = [line[0][0],line[0][1],line[0][2],line[0][3]]
    for i in range(len(column_names)):
        x.add_column(column_names[i],[line[1][i],line[2][i],line[3][i],line[4][i],line[5][i]])
    html_code = x.get_html_string()
    html_file = open('templates/table.html','w')
    html_file = html_file.write(html_code)
    




@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')



@app.route('/airbase_data')
def airbase():
    to_html_converter('airbase_data')
    return render_template('table.html')



@app.route('/titanic')
def titanic():
    to_html_converter('titanic')
    return render_template('table.html')



@app.route('/flowdata')
def flowdata():
    to_html_converter('flowdata')
    return render_template('table.html')



@app.route('/melb_data')
def melb():
    to_html_converter('melb_data')
    return render_template('table.html')






if __name__=='__main__':
    app.run(debug=True)