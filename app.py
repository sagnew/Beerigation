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
    user_input = request.form['user_input']
    suggested = get_suggestions(user_input)
    return render_template('index.html', suggested=suggested)

@app.route('/query', methods=['POST', 'GET'])
def index():
    """Allow the user to query our database."""
    query = request.form['query']
    result = ""
    if query:
        result = execute_query(query)
    return render_template('index.html', result=result)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug="true")
