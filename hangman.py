import random
from words import words

def get_word(words):
    """Get random word that doesn't have hyphen or space."""
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def game():
    """Hangman game function."""
    attempts = 7
    word = get_word(words)
    word_letters = set(word)
    guessed_letters = []

    while attempts and len(word_letters) > 0:
        if guessed_letters: # if you have made a guess, display message
            print(f"You have {attempts} lives left and have used letters: ", \
                  " ".join(guessed_letters))

        word_list = [letter if letter in guessed_letters else "-" for letter in word]
        print("Your progress: ", " ".join(word_list))

        guess = input("Guess a letter in the word: ").upper()
        print("") # line break

        if guess in word_letters:
            print("Correct!")
            word_letters.remove(guess)
            guessed_letters.append(guess)
        else:
            if guess in guessed_letters:
                print("You already guessed", guess)
            else:
                print("Incorrect!")
                guessed_letters.append(guess)
                attempts -= 1
    if attempts == 0:
        print("Game Over!")
    else:
        print("You win!")

game()
