from flask import Flask, render_template,request,redirect
from db import Database
from api import API

app = Flask(__name__)
apio=API()
dbo=Database()



## when someone hit '/' login page trigger
@app.route('/')
def index():
    return render_template('login.html')



## when someone hit '/register' login page trigger
@app.route('/register')
def register():
    return render_template('register.html')



## fetch data from registration page add in Database and do registration and redirect to login page
@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name=request.form.get("user's name")
    password=request.form.get("user's password")
    email=request.form.get("user's email")

    response=dbo.insert(name,email,password)

    if response:
        return render_template('login.html',message="Your Registration is Successful , Kindly Login to Proceed") 
    else:
        return render_template('register.html',message="This Email Already Exists , Try with Different Email")
    ## return name + " " + email + " " + password + " "



## takes email and password search in database if found then perform login
@app.route('/perform_login',methods=['post'])
def perform_login():
    password=request.form.get("user's password")
    email=request.form.get("user's email")

    response=dbo.search(email,password)

    if response:
        return redirect('/profile')
    else:
        return render_template('login.html' , message="Incorrect email and password combination")
    #return "login ho gya"



@app.route('/profile')
def profile():
    return render_template('profile.html')



@app.route('/ner',methods=['GET', 'POST'])
def ner():
    return render_template('ner.html')

@app.route('/perform_ner',methods=['post'])
def perform_ner():
    text=request.form.get('text')
    result=apio.ner(text)
    print(result)
    # return 'something'
    return render_template('ner.html',result=result)




@app.route('/sentiment_analysis',methods=['GET', 'POST'])
def sentiment_analysis():
    return render_template('sentiment.html')

@app.route('/perform_sentiment_analysis', methods=['POST'])
def perform_sentiment_analysis():

    text = request.form.get('text')

    result = apio.sentiment_analysis(text)
    print(result)
    #return 'something'

    return render_template('sentiment.html', result=result)



@app.route('/emotion_detection',methods=['GET', 'POST'])
def emotion_detection():
    return render_template('emotion.html')

@app.route('/perform_emotion_detection', methods=['POST'])
def perform_emotion_detection():

    text = request.form.get('text')

    result = apio.emotion_analysis(text)

    return render_template('emotion.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)