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
    query_type = request.form['querytype']
    suggestions = ["Nothing"]
   # if query_type == "0":
   #     suggestions = get_suggestions_by_user_ratings(user_input)
   # elif query_type == "1":
   #     suggestions = get_suggestions_by_beer_type(user_input)
   # else:
   #     suggestions = get_suggestions_by_brewery(user_input)
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
