from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/topfive')
def top_five():
    fav_guitarists = ['Jerry Garcia', 'George Harrison', 'Trey Anastasio', 'Pete Townshend', 'Jimmy Page']
    return render_template('topfive.html', guitarists = fav_guitarists)