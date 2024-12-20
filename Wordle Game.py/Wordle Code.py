import random

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
list = ["apple","berry","mango","peach","grape","boast","crave"]

# Choosing a random word from list.
word = random.choice(list)
print(word)








while True:

 try:

     # Asking for User's 5-letter word.
     answer = input("Please guess a 5-letter word: ")    # Seeing if any letters are right or wrong.
     
     # Lowercasing answer
     u_word = answer.lower()
     print(u_word)

     if u_word == word:
      print("Great Job! You guessed the word.The word is:", word)

     
     if u_word[0] == word[0]:
        print(bcolors.OKGREEN + u_word[0] + bcolors.ENDC)   
        if u_word[0] == word[1]:
             print(bcolors.WARNING + u_word[0] + bcolors.ENDC)  
        if u_word[0] == word[2]:
             print(bcolors.WARNING + u_word[0] + bcolors.ENDC)  
        if u_word[0] == word[3]:
             print(bcolors.WARNING + u_word[0] + bcolors.ENDC)  
        if u_word[0] == word[4]:
             print(bcolors.WARNING + u_word[0] + bcolors.ENDC)
        elif u_word[0] != word([0],[1],[2],[3],[4]):
             print(u_word[0])  

     if u_word[1] == word[1]:
         print(bcolors.OKGREEN + u_word[1] + bcolors.ENDC) 
         if u_word[1] == word[0]:
             print(bcolors.WARNING + u_word[1] + bcolors.ENDC) 
         if u_word[1] == word[2]:
             print(bcolors.WARNING + u_word[1] + bcolors.ENDC) 
         if u_word[1] == word[3]:
             print(bcolors.WARNING + u_word[1] + bcolors.ENDC) 
         if u_word[1] == word[4]:
             print(bcolors.WARNING + u_word[1] + bcolors.ENDC) 
         else:
             print(u_word[1])   


     if u_word[2] == word[2]:
         print(bcolors.OKGREEN + u_word[2] + bcolors.ENDC)  
         if u_word[2] == word[0]:
             print(bcolors.WARNING + u_word[2] + bcolors.ENDC) 
         if u_word[2] == word[1]:
              print(bcolors.WARNING + u_word[2] + bcolors.ENDC) 
         if u_word[2] == word[3]:
             print(bcolors.WARNING + u_word[2] + bcolors.ENDC) 
         if u_word[2] == word[4]:
             print(bcolors.WARNING + u_word[2] + bcolors.ENDC) 
         else:
             print(u_word[2])      

     if u_word[3] == word[3]:
         print(bcolors.OKGREEN + u_word[3] + bcolors.ENDC) 
         if u_word[3] == word[0]:
             print(bcolors.WARNING + u_word[3] + bcolors.ENDC) 
         if u_word[3] == word[1]:
             print(bcolors.WARNING + u_word[3] + bcolors.ENDC) 
         if u_word[3] == word[2]:
             print(bcolors.WARNING + u_word[3] + bcolors.ENDC) 
         if u_word[3] == word[4]:
             print(bcolors.WARNING + u_word[3] + bcolors.ENDC) 
         else:
             print(u_word[3])    

     if u_word[4] == word[4]:
         print(bcolors.OKGREEN + u_word[4] + bcolors.ENDC)  
         if u_word[4] == word[0]:
             print(bcolors.WARNING + u_word[4] + bcolors.ENDC) 
         if u_word[4] == word[1]:
             print(bcolors.WARNING + u_word[4] + bcolors.ENDC) 
         if u_word[4] == word[2]:
             print(bcolors.WARNING + u_word[4] + bcolors.ENDC) 
         if u_word[4] == word[3]:
             print(bcolors.WARNING + u_word[4] + bcolors.ENDC) 
         else:
             print(u_word[4])   
 except ValueError:
     print("Make sure your word is 5-digits.")    

 for u_word in range(len(word)):
     print(u_word,word[u_word])