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




#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)