import random

# Define the secret word
secret_word = "banana"

# Create a list of underscores to represent the hidden letters
hidden_word = ["_" for letter in secret_word]

# Keep track of the number of guesses
num_guesses = 0

# Loop until the word is guessed
while "_" in hidden_word:
    # Prompt the user for a guess
    guess = input("Guess a {}-letter word: ".format(len(secret_word)))
    num_guesses += 1
    
    # Check that the guess is the same length as the secret word
    if len(guess) != len(secret_word):
        print("Your guess must be {} letters long. Try again.".format(len(secret_word)))
        continue
    
    # Generate the hint
    hint = ""
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint += guess[i].upper()
        elif guess[i] in secret_word:
            hint += guess[i].lower()
        else:
            hint += "_"
    
    # Show the hint to the user
    print("Hint: {}".format(hint))
    
    # Update the hidden word with any correct guesses
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hidden_word[i] = guess[i]
    
# The word has been guessed, so display the final result
print("Congratulations, you guessed the word {} in {} guesses!".format(secret_word, num_guesses))
