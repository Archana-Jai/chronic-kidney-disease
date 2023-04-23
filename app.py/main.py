from turtle import pd
from flask import Flask, render_template, request, flash, redirect
import pickle
import numpy as np



app = Flask(__name__)
model = pickle.load(open('C:\Users\ELCOT\Downloads\CKD.pkl','rb'))

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/prediction", methods=['GET', 'POST'])
def prediction():
    return render_template('index.html')

@app.route("/home", methods=['GET', 'POST'])
def my_home():
    return render_template('index.html')


@app.route("/predict", methods = ['POST'])
def predict():

# reading the inputs given by the user
input_features = [float(x) for x in request.form.values()]
features_value = [np.array(input_features)]

features_name =['blood_urea', 'blood glucose random','anemia',
                'coronary_artery_disease','pus_cell','red_blood_cells',
                'diabetes-mellitus','pedal_edema']
df =[pd.DataFrame(features_value, columns=features_name)]

#predictions using the loaded model file
output = model.predict(df)

#showing the prediction results is a UI# showing the predictions results in a UI
 render_template('result.html',prediction_text=output)


if __name__ == '__main__':
    #running the app
	app.run(debug = True)
