from app_kingdom_hearts import app
from flask import render_template



@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/all_games')
def games_page():
    return render_template('all_games.html')

@app.route('/saga_info')
def info_page():
    return render_template('saga_info.html')

@app.route('/whats_next')
def whats_next_page():
    return render_template('whats_next.html')