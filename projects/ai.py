import random

# Create a dictionary of flashcards with hints
flashcards = {
    "Python": {
        "hint": "A popular programming language known for its simplicity and readability.",
        "answer": "A popular programming language."
    },
    "OpenAI": {
        "hint": "An organization focused on artificial intelligence research and advanced language models.",
        "answer": "An organization focused on artificial intelligence research."
    },
    "HTML": {
        "hint": "A markup language used for web development to create the structure of web pages.",
        "answer": "Hypertext Markup Language used for web development."
    },
    "CPU": {
        "hint": "The brain of a computer, responsible for executing instructions.",
        "answer": "Central Processing Unit, the brain of a computer."
    },
    "AI": {
        "hint": "The simulation of human-like intelligence in machines, making them capable of learning and decision-making.",
        "answer": "Artificial Intelligence, simulating human-like intelligence in machines."
    }
}

# Function to display a flashcard with a hint
def show_flashcard():
    card = random.choice(list(flashcards.items()))
    print(f"Question: What is {card[0]}?")
    hint = input("Would you like a hint? (yes/no): ")
    if hint.lower() == "yes":
        print(f"Hint: {card[1]['hint']}")
    input("Press Enter to reveal the answer...")
    print(f"Answer: {card[1]['answer']}\n")

# Main program loop
while True:
    print("Flashcard Application")
    print("1. Show a Flashcard")
    print("2. Exit")
    choice = input("Select an option (1/2): ")

    if choice == "1":
        show_flashcard()
    elif choice == "2":
        print("Exiting the flashcard application. Goodbye!")
        break
    else:
        print("Invalid option. Please select 1 or 2.")
