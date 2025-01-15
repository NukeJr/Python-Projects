import random

guesses = 6

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

print ("Welcome To Wordle!")


# Making a list of words that can be guessed.
list = ('https://media2-production.mightynetworks.com/asset/a6979138-b83f-4ebe-a5fe-675d20c1b164/fiveLetterWords.txt#_gl=1*1asp8an*_ga*NzU0MjA3NTY0LjE3MjA0OTk5NTk.*_ga_T49FMYQ9FZ*MTczNjg4ODgwNC4xNDYuMS4xNzM2ODg5MTc4LjAuMC4w*_ga_NEGJ2SXNP7*MTczNjg4ODgwOS4xNDQuMS4xNzM2ODg5MTc3LjUxLjAuMA..')
for cheese in list:
      print(cheese)

# Choosing a random word from list.
word = random.choice(list)
# print(word)

while True:

 try:

     # Asking for User's 5-letter word.
     answer = input("Please guess a 5-letter word: ")    # Seeing if any letters are right or wrong.

     # Lowercasing answer
     u_word = answer.lower()
     
     if u_word == word:
       print("Great Job! You guessed the word:", word)
       break
     if len(u_word) != 5:
           print("Invalid Answer")
           continue
     for letter_index in range(len(u_word)):
           if u_word [letter_index] == word[letter_index]:
                 print("Green")


     if u_word[0] == word[0]:
        print(bcolors.OKGREEN + u_word[0] + bcolors.ENDC)   
     elif u_word[0] == word[1]:
             print(bcolors.WARNING + u_word[0] + bcolors.ENDC)
     elif u_word[0] == word[2]:
             print(bcolors.WARNING + u_word[0] + bcolors.ENDC)
           #  continue  
     elif u_word[0] == word[3]:
             print(bcolors.WARNING + u_word[0] + bcolors.ENDC) 
           #  continue 
     elif u_word[0] == word[4]:
             print(bcolors.WARNING + u_word[0] + bcolors.ENDC)
           #  continue
     else:
             print(u_word[0])  

     if u_word[1] == word[1]:
         print(bcolors.OKGREEN + u_word[1] + bcolors.ENDC) 
     elif u_word[1] == word[0]:
             print(bcolors.WARNING + u_word[1] + bcolors.ENDC) 
     elif u_word[1] == word[2]:
             print(bcolors.WARNING + u_word[1] + bcolors.ENDC) 
     elif u_word[1] == word[3]:
             print(bcolors.WARNING + u_word[1] + bcolors.ENDC) 
     elif u_word[1] == word[4]:
             print(bcolors.WARNING + u_word[1] + bcolors.ENDC) 
     else:
          print(u_word[1])   

     if u_word[2] == word[2]:
         print(bcolors.OKGREEN + u_word[2] + bcolors.ENDC)  
     elif u_word[2] == word[0]:
             print(bcolors.WARNING + u_word[2] + bcolors.ENDC) 
     elif u_word[2] == word[1]:
              print(bcolors.WARNING + u_word[2] + bcolors.ENDC) 
     elif u_word[2] == word[3]:
             print(bcolors.WARNING + u_word[2] + bcolors.ENDC) 
     elif u_word[2] == word[4]:
             print(bcolors.WARNING + u_word[2] + bcolors.ENDC) 
     else:
             print(u_word[2])      

     if u_word[3] == word[3]:
         print(bcolors.OKGREEN + u_word[3] + bcolors.ENDC) 
     elif u_word[3] == word[0]:
             print(bcolors.WARNING + u_word[3] + bcolors.ENDC) 
     elif u_word[3] == word[1]:
             print(bcolors.WARNING + u_word[3] + bcolors.ENDC) 
     elif u_word[3] == word[2]:
             print(bcolors.WARNING + u_word[3] + bcolors.ENDC) 
     elif u_word[3] == word[4]:
             print(bcolors.WARNING + u_word[3] + bcolors.ENDC) 
     else:
             print(u_word[3])    

     if u_word[4] == word[4]:
         print(bcolors.OKGREEN + u_word[4] + bcolors.ENDC)  
     elif u_word[4] == word[0]:
             print(bcolors.WARNING + u_word[4] + bcolors.ENDC) 
     elif u_word[4] == word[1]:
             print(bcolors.WARNING + u_word[4] + bcolors.ENDC) 
     elif u_word[4] == word[2]:
             print(bcolors.WARNING + u_word[4] + bcolors.ENDC) 
     elif u_word[4] == word[3]:
             print(bcolors.WARNING + u_word[4] + bcolors.ENDC) 
     else:
             print(u_word[4])

 
  # Making sure the code dosen't blow up if anything in the code is wrong
 except ValueError:
     print("Make sure your word is 5-digits.")    

  #for u_word in range(len(word)):
  #   print(u_word,word[u_word])
 if guesses != 1:
  guesses -= 1
 else: 
    print(f"You have no guesses remaining. The word is:",word)
    break
 print (f"You have",guesses,"guesses left.")
 continue