from flask import Flask,render_template,url_for,redirect,flash,request
from forms import SignupForm,LoginForm
from flask_sqlalchemy import SQLAlchemy
import sqlite3
app=Flask(__name__)
app.config['SECRET_KEY']='linktree'
@app.route('/')
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/signup",methods=['POST','GET'])
def signup():
    form=SignupForm()
    if form.validate_on_submit():
        connection=sqlite3.connect("users_data.db")
        cursor=connection.cursor()
        sqlite_insert="""INSERT INTO users(name,password) VALUES(?,?);"""
        username=form.username.data
        password=form.password.data
        print(username,password)
        data_tuple=(username,password)
        cursor.execute(sqlite_insert,data_tuple)
        connection.commit()
        flash(f'Account created successfully for {form.username.data}')
        return redirect(url_for('login'))
    return render_template('signup.html',title='Signup',form=form)

@app.route("/account")
@app.route("/login",methods=['POST','GET'])
def login():
   
    if request.method=='POST':
        connection=sqlite3.connect('users_data.db')
        cursor=connection.cursor()

        name=request.form['name']
        password=request.form['password']

        # print(name,password)

        query="SELECT name,password FROM users where name='"+name+"' and password='"+password+"'" 
        cursor.execute(query)

        results=cursor.fetchall() 

        if len(results)==0:
            print("Incorrect Credentials provided.Try Again!")
        else:
<<<<<<< HEAD
            return render_template('account.html')
    return render_template('login.html')           
=======
            flash(f'Login unsuccessful for {form.username.data}', category="danger")
    return render_template('login.html',title='login',form=form)
>>>>>>> 8bf804c3471524a8374f58c8f4b87ec7a18b31da

if __name__=="__main__":
    app.run(debug=True)        
