import os
import json
from flask import Flask, render_template, request
import db
from arrayOfBeers import arrayOfBeers

#set up a list of all beers for autocompletions
autocompletions = arrayOfBeers

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    """Respond with index page."""
    return render_template('index.html', autocompletions=json.dumps(autocompletions))

@app.route('/recommend', methods=['POST', 'GET'])
def recommend():
    """Respond with index page."""
    user_input = request.form['beer']
    query_type = request.form['querytype']
    suggestions = ["Nothing"]

    if query_type == "0":
        suggestions = db.sqlVoter(user_input)
    elif query_type == "1":
        suggestions = db.sqlType(user_input)
    else:
        suggestions = db.sqlManf(user_input)

    return render_template('results.html', user_input=user_input, suggestions=suggestions, autocompletions=json.dumps(autocompletions))

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
    else:
        result = "No query!"
    return render_template('query.html', result=result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug="true")
