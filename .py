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

previous_guesses = []

print(random_word)

while guesses > 0:
        try:

                answer = input('Please guess a 5-letter word:').lower()

                if len(answer) != 5:
                        print("Make sure your word is 5 characters. ")
                        continue 

                if answer not in words:
                        print("Please enter a valid word from the word list.")

                if answer == random_word:
                        print("Great Job! You guessed the word:", random_word)
                        break
                if answer not in previous_guesses:
                        previous_guesses.append(answer)

                print("\nPrevious guesses: ")
                for guess in previous_guesses:
                        print(guess)

                word_used = [False] * 5  # Track Letters already matched in random_word
                guess_used = [False] * 5  # Track Letters already matched in the guess

                # FIRST PASS: Green feedback for exact matches (correct position)
                for i in range(5):
                        if answer[i] == random_word[i]:
                                print(bcolors.OKGREEN + answer[i] + bcolors.ENDC, end="")
                                word_used[i] = True  # Mark this position in random_word as used
                                guess_used[i] = True  # Mark this position in the guess as used
                        else:
                                print(answer[i], end="")

                print()

                # SECOND PASS: Yellow feedback for wrong position (exists in word but wrong position)
                for i in range(5):
                        if not guess_used[i]:  # If this letter hasn't been used already
                                for j in range(5):
                                        if not word_used[j] and answer[i] == random_word[j]:  # Check if the letter exists in random_word but in the wrong position
                                                print(bcolors.WARNING + answer[i] + bcolors.ENDC, end="")
                                                word_used[j] = True  # Mark this letter as used in random_word
                                                break
                                else:
                                        print(answer[i], end="")  # If no match found, print normally

                print()

                guesses -= 1 
                print(f"You have {guesses} guesses left.")

                if guesses == 0:
                        print(f"You have no guesses remaining. The word was: {random_word}")
        except ValueError:
                print("Please enter a valid word.")
