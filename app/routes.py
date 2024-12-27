from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Adam'}
    posts = [
        {
            'author': {'username': 'George Foreman'},
            'body': "If only I had my Foreman grill back in the day I could've slapped Ali silly with the greatest burgers he had."
            
        },
        {
            'author': {'username': 'Muhammed Ali from the Grave'},
            'body': "What was that George? You're cooking me dinner? I knew you were a girl all along!"
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
    
