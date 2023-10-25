from flask import Flask, request, jsonify

app = Flask(__name__)

flashcards = []

@app.route('/create_flashcard', methods=['POST'])
def create_flashcard():
    data = request.get_json()

    if 'question' not in data or 'answer' not in data:
        return jsonify({'error': 'Missing question or answer'}), 400

    question = data['question']
    answer = data['answer']

    flashcard = {'question': question, 'answer': answer}
    flashcards.append(flashcard)

    return jsonify({'message': 'Flashcard created successfully'})

@app.route('/get_flashcards', methods=['GET'])
def get_flashcards():
    return jsonify({'flashcards': flashcards})

@app.route('/update_flashcard/<int:index>', methods=['PUT'])
def update_flashcard(index):
    if index < 0 or index >= len(flashcards):
        return jsonify({'error': 'Invalid index'}), 400

    data = request.get_json()

    if 'question' not in data or 'answer' not in data:
        return jsonify({'error': 'Missing question or answer'}), 400

    flashcards[index]['question'] = data['question']
    flashcards[index]['answer'] = data['answer']

    return jsonify({'message': 'Flashcard updated successfully'})

@app.route('/delete_flashcard/<int:index>', methods=['DELETE'])
def delete_flashcard(index):
    if index < 0 or index >= len(flashcards):
        return jsonify({'error': 'Invalid index'}), 400

    deleted_flashcard = flashcards.pop(index)

    return jsonify({'message': 'Flashcard deleted successfully', 'deleted_flashcard': deleted_flashcard})

if __name__ == '__main__':
    app.run(debug=True)







