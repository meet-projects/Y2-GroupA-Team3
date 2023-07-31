# from flask import Flask, render_template, request, redirect, url_for, flash
from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'
config = {
  "apiKey": "AIzaSyCWJvL11O1Q983LXR218a51EGNZHUHOMps",
  "authDomain": "groupprojectweb-5d2dd.firebaseapp.com",
  "projectId": "groupprojectweb-5d2dd",
  "storageBucket": "groupprojectweb-5d2dd.appspot.com",
  "messagingSenderId": "521418284281",
  "appId": "1:521418284281:web:20ae20233d2020f9b75628",
  "measurementId": "G-5WB87QXG2D",
  "databaseURL" : "https://groupprojectweb-5d2dd-default-rtdb.europe-west1.firebasedatabase.app/"
};

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db= firebase.database()
#Code goes below here

@app.route('/' , methods=['GET', 'POST'])
def generalform():
    if request.method == 'POST':
        name= request.form['name']
        gender= request.form['sex']
        # dob= request.form['dob']
        bg= request.form['bg']
        illness= request.form.get('illness')
        meds= request.form['meds']
        age = request.form['age']
        signs = request.form['signs']
        skin_prick_test = request.form['skin_prick_test']
        blood_test_ige = request.form['blood_test_ige']
        food_challenge = request.form['food_challenge']
        food_allergies = request.form.getlist('food_allergies')
        other_foods = request.form['other_foods']
        additional_allergens = request.form.getlist('additional_allergens')
        animals_specify = request.form['animals_specify']
        trees_specify = request.form['trees_specify']
        other_plants_specify = request.form['other_plants_specify']
        other_allergens_specify = request.form['other_allergens_specify']
        other_allergic_diseases = request.form.getlist('other_allergic_diseases')
        preventive_treatment = request.form.getlist('preventive_treatment')
        family_morbidity = request.form.getlist('family_morbidity')
        family_morbidity_details = request.form['family_morbidity_details']
        skin_prick_test = request.form['skin_prick_test']
        blood_test_ige = request.form['blood_test_ige']
        food_challenge = request.form['food_challenge']
        food_allergies = request.form.getlist('food_allergies')
        other_foods = request.form['other_foods']
        additional_allergens = request.form.getlist('additional_allergens')
        animals_specify = request.form['animals_specify']
        trees_specify = request.form['trees_specify']
        other_plants_specify = request.form['other_plants_specify']
        other_allergens_specify = request.form['other_allergens_specify']
        other_allergic_diseases = request.form.getlist('other_allergic_diseases')
        preventive_treatment = request.form.getlist('preventive_treatment')
        family_morbidity = request.form.getlist('family_morbidity')
        family_morbidity_details = request.form['family_morbidity_details']
        patient_data = {
            "name": name,
            "gender": gender,
            # "dob": dob,
            "blood_group": bg,
            "illness": illness,
            "medications": meds,
            "age": age,
            "signs": signs,
            "skin_prick_test": skin_prick_test,
            "blood_test_ige": blood_test_ige,
            "food_challenge": food_challenge,
            "food_allergies": food_allergies,
            "other_foods": other_foods,
            "additional_allergens": additional_allergens,
            "animals_specify": animals_specify,
            "trees_specify": trees_specify,
            "other_plants_specify": other_plants_specify,
            "other_allergens_specify": other_allergens_specify,
            "other_allergic_diseases": other_allergic_diseases,
            "preventive_treatment": preventive_treatment,
            "family_morbidity": family_morbidity,
            "family_morbidity_details": family_morbidity_details
        }
        db.child("Patients").push(patient_data)
        return render_template('index.html')
    else: 
        return render_template('index.html')




#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)