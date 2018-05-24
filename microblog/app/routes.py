from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Natan"}
    posts = [
        {
            "author" : {'username' : 'John'},
            'body' :   'Beautifuly day in Portland!'
        },
        {
            "author": {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',  title='Home', user=user, posts=posts)
