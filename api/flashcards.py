from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for flashcards
flashcards = [
    {"id": 1, "question": "What is the capital of France?", "answer": "Paris"},
    {"id": 2, "question": "What is 2 + 2?", "answer": "4"},
    # Add more flashcards as needed
]

# API endpoint to get all flashcards
@app.route('/flashcards', methods=['GET'])
def get_flashcards():
    return jsonify({'flashcards': flashcards})

# API endpoint to get a specific flashcard by ID
@app.route('/flashcards/<int:flashcard_id>', methods=['GET'])
def get_flashcard(flashcard_id):
    flashcard = next((card for card in flashcards if card['id'] == flashcard_id), None)
    if flashcard:
        return jsonify({'flashcard': flashcard})
    else:
        return jsonify({'message': 'Flashcard not found'}), 404

# API endpoint to create a new flashcard
@app.route('/flashcards', methods=['POST'])
def create_flashcard():
    new_flashcard = {
        'id': len(flashcards) + 1,
        'question': request.json['question'],
        'answer': request.json['answer']
    }
    flashcards.append(new_flashcard)
    return jsonify({'flashcard': new_flashcard}), 201

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
