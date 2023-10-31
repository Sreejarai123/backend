from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Index Endpoint
@app.route('/', methods=['GET'])
def index():
    """
    Renders the HTML template for the GrammarBot Checker.
    This endpoint is responsible for displaying the form where users can input text and language.
    """
    return render_template('index.html')

# Check Grammar Endpoint
@app.route('/check_grammar', methods=['POST'])
def check_grammar():
    """
    Handles the form submission from the index page.
    It makes a POST request to the GrammarBot API with the provided text and language,
    then returns the JSON response from the GrammarBot API.
    If there's an error, it returns a JSON response with an error message.
    """
    text = request.form.get('text')
    language = request.form.get('language', 'en-US')

    # URL and endpoint for GrammarBot API
    url = 'https://grammarbot.p.rapidapi.com/check'

    # Set your RapidAPI key
    rapidapi_key = '9fb198c26fmsh98120fcb28c72fdp100517jsn7aa4c1e9a84c'

    # Set headers for the request
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-RapidAPI-Key': '9fb198c26fmsh98120fcb28c72fdp100517jsn7aa4c1e9a84c',
        'X-RapidAPI-Host': 'grammarbot.p.rapidapi.com'
    }

    # Set data for the request
    data = {
        'text': text,
        'language': language
    }

    # Make the POST request
    response = requests.post(url, headers=headers, data=data)

    # Check the response
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': f"Error: {response.status_code}, {response.text}"}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8086, debug=True)


