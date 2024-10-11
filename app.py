# Flask app to serve the Retro Achievements widget
import os
from flask import Flask, render_template, request, jsonify
import requests
import re
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv('API_KEY')
API_USERNAME = os.getenv('API_USERNAME')

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/recent-game-overlay/<username>', methods=['GET'])
def overlay(username):
    # Input validation for username
    if not username or not re.match(r'^[A-Za-z0-9_]{3,20}$', username):
        return 'Invalid username provided', 400
    return render_template('recent_game_overlay.html', username=username)

@app.route('/recent-achievement-overlay/<username>', methods=['GET'])
def achievement_overlay(username):
    # Input validation for username
    if not username or not re.match(r'^[A-Za-z0-9_]{3,20}$', username):
        return 'Invalid username provided', 400
    return render_template('recent_achievement_overlay.html', username=username)

@app.route('/api/user-summary', methods=['POST'])
def user_summary():
    data = request.get_json()
    username = data.get('username')

    # Input validation for username
    if not username or not re.match(r'^[A-Za-z0-9_]{3,20}$', username):
        return jsonify({'error': 'Invalid username provided'}), 400

    api_key = API_KEY
    url = 'https://retroachievements.org/API/API_GetUserSummary.php'
    params = {
        'z': API_USERNAME,
        'y': api_key,
        'u': username
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Failed to fetch user summary', 'details': str(e)}), 500

    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch user summary', 'status_code': response.status_code}), response.status_code

    return jsonify(response.json())

@app.route('/api/recent-achievement', methods=['POST'])
def recent_achievement():
    data = request.get_json()
    username = data.get('username')

    # Input validation for username
    if not username or not re.match(r'^[A-Za-z0-9_]{3,20}$', username):
        return jsonify({'error': 'Invalid username provided'}), 400

    api_key = API_KEY
    url = 'https://retroachievements.org/API/API_GetUserRecentAchievements.php'
    params = {
        'y': api_key,
        'u': username,
        'm': 43800
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Failed to fetch recent achievements', 'details': str(e)}), 500

    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch recent achievements', 'status_code': response.status_code}), response.status_code

    return jsonify(response.json())

@app.route('/api/game-info', methods=['POST'])
def game_info():
    data = request.get_json()
    username = data.get('username')
    game_id = data.get('gameId')

    # Input validation for username
    if not username or not re.match(r'^[A-Za-z0-9_]{3,20}$', username):
        return jsonify({'error': 'Invalid username provided'}), 400

    api_key = API_KEY
    url = 'https://retroachievements.org/API/API_GetGameInfoAndUserProgress.php'
    params = {
        'z': API_USERNAME,
        'y': api_key,
        'u': username,
        'g': game_id
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Failed to fetch game info', 'details': str(e)}), 500

    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch game info', 'status_code': response.status_code}), response.status_code

    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)