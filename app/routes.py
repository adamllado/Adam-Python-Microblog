from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Adam'}
    posts = [
        {
            'author': {'username': 'Monica'},
            'body': "My bf tells me how much my ass turns him on! Should I show him a pic tehe??"
            
        },
        {
            'author': {'username': 'Michelle'},
            'body': "Monica, you know flat asses don't turn anyone on gurl. stop lying to yourself Mhmm."
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

