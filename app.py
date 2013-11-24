import os
from flask import Flask, render_template, request
from beer_utils import get_beer_suggestions


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    """Respond with index page."""
    return render_template('index.html')

@app.route('/recommend', methods=['POST', 'GET'])
def recommend():
    """Respond with index page."""
    user_beer = request.form['beer']
    suggested_beers = get_beer_suggestions(user_beer)
    return render_template('index.html', suggested_beers=suggested_beers)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug="true")
