import random
from words import words

def game():
    attempts = 7
    guessed = []
    word = random.choice(words)
    letters = set(word)

    while attempts:
        guess_state = ""
        for char in word:
            guess_state += "_ "

        chars_to_go = guess_state.count("_")

        print(f"Your word is {len(word)} characters long:", guess_state)
        guess = input("Guess a letter in the word: ")

        if guess in guessed:
            print("Already guessed", guess.upper())
        guessed.append(guess)

        word_list = [letter if letter in word else "_ " for letter in word]
        print(word_list)

game()
