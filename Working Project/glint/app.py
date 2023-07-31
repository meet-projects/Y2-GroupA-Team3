from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase
import os
firebaseConfig = {
  "apiKey": "AIzaSyA15N1aqsF6wgGhR1ioCLucpBkKZLJA5hg",
  "authDomain": "ukkomeety2.firebaseapp.com",
  "projectId": "ukkomeety2",
  "storageBucket": "ukkomeety2.appspot.com",
  "messagingSenderId" : "511419561452",
  "appId": "1:511419561452:web:f4b3a43ec751715f9efcc9",
  "measurementId" : "G-5SSGNXY25Y",
  "databaseURL" : "https://ukkomeety2-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()








app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/' , methods=['GET' , 'POST'])
def home():
	return render_template("index.html")

@app.route('/login' , methods=['GET' , 'POST'])
def login():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']

		login_session['user'] = auth.sign_in_with_email_and_password(email , password)

		uname = db.child("Users").child(login_session['user']['localId']).get().val()
		login_session['uname'] = uname

		return redirect(url_for('doctor'))

	return render_template("login.html")

@app.route('/signup' , methods=['POST'])
def signup():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		try:
			login_session['user'] = auth.create_user_with_email_and_password(email, password)
			userid = login_session['user']['localId']
			user = {
				"email": email,
				"username": request.form['username']
			}
			db.child("Users").child(userid).set(user)
			uname = db.child("Users").child(login_session['user']['localId']).get().val()
			login_session['uname'] = uname['username']
			return redirect(url_for('doctor'))
		except:
			return redirect(url_for('login'))
@app.route('/MedicalHub' , methods=['GET', 'POST'])
def doctor():
		if request.method == 'POST':
			name = request.form['name']
			gender = request.form['sex']
			# dob= request.form['dob']
			bg = request.form['bg']
			illness = request.form.get('illness')
			meds = request.form['meds']
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
			db.child("Users").child(login_session['user']['localId']).child("patientData").push(patient_data)
			return render_template("doctor.html" , sucsses=True)
		return render_template("doctor.html" , sucsses=False)

@app.route('/view' , methods=['GET'])
def view():
	patientData = db.child("Users").child(login_session['user']['localId']).child("patientData").get().val()
	return render_template("view.html" , data=patientData)
if __name__ == '__main__':
    app.run(debug=True)