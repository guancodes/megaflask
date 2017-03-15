from flask import render_template, flash, redirect
from app import app
# if you want to directly import from a package, then the
# object to import needs to be defined inside __init__.py
# a module is also a package
# a package is a folder that contains __init__.py
# a module is a .py file
from .forms import LoginForm

@app.route('/') # this app is my Flask app from __init__.py
@app.route('/index')
def index():
	user = {'nickname': 'Michael'}
	posts = [{'author':{'nickname':'John'}, 'body': 'Beautiful day in Portland'},{'author':{'nickname':'James'},'body':'The Avengers movie was so cool'}]
	return render_template('index.html', user = user, posts = posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID = "%s", remember_me = %s' % (form.openid.data,str(form.remember_me.data)))
		return redirect('/index')
	return render_template('login.html', title = 'Sign In', form = form, providers=app.config['OPENID_PROVIDERS'])
