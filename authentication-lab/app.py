from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {
  "apiKey": "AIzaSyCtTNHBjczxTp8LYMG3LCIN6mhysqomptM",
  "authDomain": "proj1-d4176.firebaseapp.com",
  "projectId": "proj1-d4176",
  "storageBucket": "proj1-d4176.appspot.com",
  "messagingSenderId": "484315964747",
  "appId": "1:484315964747:web:72531f52840ac1bde834ce",
  "measurementId": "G-WZJ5YGS1PT",
  "databaseURL": "",
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
            error = "Authentication failed"
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)