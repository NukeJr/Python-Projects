import random

def choose_word():
  list = ["apple","cream","boast","stray","berry","pear","given",]
  return random.choice(list)

def wordle():
 
 word = choose_word()
 print("Welcome To Wordle")
 print(word)
 
 for remaning_guesses in range(6,-1, -1):
     u_word = input("Guess a 5-letter Word: ").lower()
  
     if not u_word.isalpha():
      print("Invalid word please try with only letters.")
     elif len(u_word) != 5:
      print("You word is not 5-digits long.")
     else:
      print(f"You have a valid guess: {u_word}")
      if u_word == word:
        print("You guessed the word you Win!")
      else: 
        print("You have {remaning_guess}")
     

wordle()


