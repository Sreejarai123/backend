from flask import Flask, request, jsonify
from grammarbot import GrammarBot

app = Flask(__name__)

@app.route('/check-grammar', methods=['POST'])
def check_grammar():
    data = request.get_json()
    text = data.get('text', '')
    language = data.get('language', 'en-US')

    # Using GrammarBot for simplicity, install it first: pip install grammarbot
    bot = GrammarBot(language)
    result = bot.check(text)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

