from flask import Flask,render_template,url_for,redirect,flash
from forms import SignupForm,LoginForm
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
        flash(f'Account created successfully for {form.username.data}', category="success")
        return redirect(url_for('login'))
    return render_template('signup.html',title='Signup',form=form)

@app.route("/login",methods=['POST','GET'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data=='' and form.data.password.data=='':
            flash(f'Logged in successfully for {form.username.data}', category="success")
            return redirect(url_for('account'))
        else:
            flash(f'Login unsuccessful for {form.username.data}', category="danger")
            return render_template('login.html',title='login',form=form)

if __name__=="__main__":
    app.run(debug=True)        