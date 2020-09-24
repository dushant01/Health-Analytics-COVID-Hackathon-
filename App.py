from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler,LabelEncoder

app = Flask(__name__)

model = pickle.load(open("ANN.pkl", 'rb'))


@app.route('/',methods=['GET'])
def Home():
    return render_template('home.html')

standard_to = StandardScaler()


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Department = (request.form["Department"])
        if (Department == 'TB & Chest disease'):
            Department = 0
        elif (Department == 'anesthesia'):
            Department = 1
        elif (Department == 'gynecology'):
            Department = 2
        elif (Department == 'radiotherapy'):
            Department = 3
        elif (Department == 'surgery'):
            Department = 4
        Bed = int(request.form["Bed Grade"])
        Type_of_Admission = (request.form["Type of Admission"])
        if (Type_of_Admission == 'Emergency'):
            Type_of_Admission = 0
        elif (Type_of_Admission == 'Trauma'):
            Type_of_Admission = 1
        elif (Type_of_Admission== 'Urgent'):
            Type_of_Admission = 2
        Severity_of_Illness= (request.form["Severity of Illness"])
        if (Severity_of_Illness == 'Extreme'):
            Severity_of_Illness = 0
        elif (Severity_of_Illness == 'Minor'):
            Severity_of_Illness = 1
        elif (Severity_of_Illness == 'Moderate'):
            Severity_of_Illness = 2
        Age = (request.form["Age"])
        if (Age == 'Age[0-10]'):
            Age = 0
        elif (Age == 'Age[11-20]'):
            Age = 1
        elif (Age == 'Age[21-30]'):
            Age = 2
        elif (Age == 'Age[31-40]'):
            Age = 3
        elif (Age == 'Age[41-50]'):
            Age = 4
        elif (Age == 'Age[51-60]'):
            Age = 5
        elif (Age == 'Age[61-70]'):
            Age = 6
        elif (Age == 'Age[71-80]'):
            Age = 7
        elif (Age == 'Age[81-90]'):
            Age = 8
        elif (Age == 'Age[91-100]'):
            Age = 9
        Amount = (int(request.form["Amount Deposit"]))
        print(Amount)
        array= [Department,Amount,Age,Severity_of_Illness,Bed,Type_of_Admission]
        final_features = [np.array(array)]
        Stay_test = model.predict([[Department,Amount,Age,Severity_of_Illness,Bed,Type_of_Admission]])

        Stay = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100',
                'More than 100 Days']
        #a = LabelEncoder()
        #a.fit_transform(Stay)
        #list(a.inverse_transform([0]))
        a = []
        if Stay_test == 0:
            return render_template('home.html',prediction_text="Person will stay in Hospital {} days approx.".format(Stay[0]))
        elif Stay_test == 1:
            return render_template('home.html',prediction_text="Person will stay in Hospital {} days approx.".format(Stay[1]))
        elif Stay_test == 2:
            return render_template('home.html', prediction_text="Person will stay in Hospital {} days approx.".format(Stay[2]))

        elif Stay_test == 3:
            return render_template('home.html', prediction_text="Person will stay in Hospital {} days approx.".format(Stay[3]))
        elif Stay_test == 4:
            return render_template('home.html', prediction_text="Person will stay in Hospital {} days approx.".format(Stay[4]))
        elif Stay_test == 5:
            return render_template('home.html', prediction_text="Person will stay in Hospital {} days approx.".format(Stay[5]))
        elif Stay_test == 6:
            return render_template('home.html', prediction_text="Person will stay in Hospital {} days approx.".format(Stay[6]))
        elif Stay_test == 7:
            return render_template('home.html', prediction_text="Person will stay in Hospital {} days approx.".format(Stay[7]))
        elif Stay_test == 8:
            return render_template('home.html', prediction_text="Person will stay in Hospital {} days approx.".format(Stay[8]))
        elif Stay_test == 9:
            return render_template('home.html', prediction_text="Person will stay in Hospital {} days approx.".format(Stay[9]))
        elif Stay_test == 10:
            return render_template('home.html', prediction_text="Person will stay in Hospital {} days approx.".format(Stay[10]))
        else:
            return render_template('home.html')





if __name__ == "__main__":
    app.run(debug=True)