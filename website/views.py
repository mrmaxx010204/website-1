from flask import render_template,  flash, redirect, url_for, session,request, logging
from passlib.hash import sha256_crypt

from website import app
from forms import RegisterForm

#from website.database import db_session


@app.route('/')
def index():
    return render_template('index.html')


#routing the register request
@app.route('/register', methods =['GET','POST'])
def register():
    form = RegisterForm(request.form)
    
    if request.method == 'POST' and form.validate():
        
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        
        return redirect(url_for('index'))


    return render_template('register.html', form=form)

@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm(request.form)

    if request.method == 'GET' and form.validate():

        username = form.username.data
        password = sha256_crypt.decrypt(str(form.password.data))

        return redirect(url_for('index'))
    return render_template('login.html', form = form)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/addpost', methods = ['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    return '<h1>Title: {}  Subtitle: {} Author: {} Content: {}</h1>'.format(title, subtitle, author, content)

