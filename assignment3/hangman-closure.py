def make_hangman(secret_word):

    guesses = []

    def hangman_closure(letter):

        guesses.append(letter)

        display = ""

        for character in secret_word:

            if character in guesses:
                display += character
            else:
                display += "_"

        print(display)

        for character in secret_word:

            if character not in guesses:
                return False

        return True

    return hangman_closure

secret_word = input("Enter the secret word: ")

game = make_hangman(secret_word)

finished = False

while not finished:

    guess = input("Guess a letter: ")

    finished = game(guess)

print("Congratulations! You guessed the word!")