from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!',
            'timestamp': '2 minutes ago'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!',
            'timestamp': '5 minutes ago'
        },
        {
            'author': {'nickname': 'Liz'},
            'body': 'What a dayyyy, what a day!',
            'timestamp': '1 hour ago'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)