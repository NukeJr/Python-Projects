import os
import random

guesses = 6

# Read current streak from a file
def read_win_streak():
    try:
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, "Wordle.py")
        with open(file_path) as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 0 

def write_win_streak():
    print('write_win_streak')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print('Welcome To Wordle!')

# Load 5-letter words from the file
file = "fiveLetterWords.txt"
with open(file, 'r') as f:
    words = [line.rstrip() for line in f if len(line.rstrip()) == 5]

random_word = random.choice(words)  # Random word guess

# List to keep track of previous guesses
previous_guesses = []

def color_word(word, random_word):
    """
    Function to apply coloring to the word based on feedback from the random_word.
    Returns the word as a string with color codes.
    """
    word_used = [False] * 5  # Track Letters already matched in random_word
    guess_used = [False] * 5  # Track Letters already matched in the guess
    colored_word = []

    # FIRST PASS: Green feedback for exact matches (correct position)
    for i in range(5):
        if word[i] == random_word[i]:
            colored_word.append(bcolors.OKGREEN + word[i] + bcolors.ENDC)
            word_used[i] = True
            guess_used[i] = True
        else:
            colored_word.append(word[i])

    # SECOND PASS: Yellow feedback for wrong position (exists in word but wrong position)
    for i in range(5):
        if not guess_used[i]:  # If this letter hasn't been used already
            for j in range(5):
                if not word_used[j] and word[i] == random_word[j]:  # Check if the letter exists in random_word but in the wrong position
                    colored_word[i] = bcolors.WARNING + word[i] + bcolors.ENDC
                    word_used[j] = True
                    break

    return ''.join(colored_word)

while guesses > 0:
    try:
        answer = input('Please guess a 5-letter word: ').lower()

        if len(answer) != 5:
            print("Make sure your word is 5 characters. ")
            continue

        # Add the current guess to the previous guesses list
        previous_guesses.append(answer)

        # Print the previous guesses with colored output, except for the first guess
        if len(previous_guesses) > 1:
            print("\nPrevious guesses:")
            for guess in previous_guesses[:-1]:  # All except the current guess
                print(color_word(guess, random_word))

        # Color the current guess and print it
        print(color_word(answer, random_word))

        if answer == random_word:
            print("Great Job! You guessed the word:", random_word)
            break

        guesses -= 1
        # Now display the remaining guesses after feedback
        print(f"You have {guesses} guesses left.")

        if guesses == 0:
            print(f"You have no guesses remaining. The word was: {random_word}")

    except ValueError:
        print("Please enter a valid word.")
