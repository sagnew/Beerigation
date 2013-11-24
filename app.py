import os
from flask import Flask, render_template, request
from beer_utils import get_suggestions, execute_query


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    """Respond with index page."""
    return render_template('index.html')

@app.route('/recommend', methods=['POST', 'GET'])
def recommend():
    """Respond with index page."""
    user_input = request.form['beer']
    suggestions = get_suggestions(user_input)
    suggestions = ["Guiness stout", "Lucky Lager", "Newcastle Brown Ale"]
    return render_template('results.html', user_input=user_input, suggestions=suggestions)

@app.route('/query', methods=['POST', 'GET'])
def query():
    """Allow the user to query our database."""
    return render_template('query.html', result="Results display here")

@app.route('/execute', methods=['POST', 'GET'])
def execute():
    """Allow the user to query our database."""
    query = request.form['query']
    result = ""
    if query:
        result = execute_query(query)
    result = "No results!"
    return render_template('query.html', result=result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug="true")
