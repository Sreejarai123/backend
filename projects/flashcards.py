import random

# Create a dictionary of flashcards
flashcards = {
    "Python": "A popular programming language.",
    "OpenAI": "An organization focused on artificial intelligence research.",
    "HTML": "Hypertext Markup Language used for web development.",
    "CPU": "Central Processing Unit, the brain of a computer.",
    "AI": "Artificial Intelligence, simulating human-like intelligence in machines."
}

# Function to display a random flashcard
def show_flashcard():
    card = random.choice(list(flashcards.items()))
    print(f"Question: What is {card[0]}?")
    input("Press Enter to reveal the answer...")
    print(f"Answer: {card[1]}\n")

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
