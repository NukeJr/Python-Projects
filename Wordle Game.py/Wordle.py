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
list = ["apple", "grape", "lemon", "peach", "plumb", "stone", "shine", "flute", "charm", "brisk", 
"laser", "prong", "skate", "tiger", "flick", "drain", "smile", "march", "stark", "track", 
"broil", "roast", "swoop", "flame", "snack", "bloom", "straw", "grasp", "twist", "clash", 
"light", "flock", "mirth", "plaza", "sweep", "swirl", "gloom", "tramp", "spike", "blaze", 
"creek", "cloud", "sword", "stunt", "crisp", "storm", "pearl", "brake", "grape", "swoop", 
"trend", "slice", "pouch", "sheer", "twirl", "glare", "flood", "roast", "drift", "stale", 
"pound", "beach", "flash", "swank", "stare", "twing", "spare", "gale", "brisk", "scout",
"plumb", "grape", "track", "drift", "flame", "swoop", "shine", "stone", "grasp", "spike",
"flock", "spool", "tramp", "glare", "gloom", "snack", "cloud", "brake", "grind", "tiger",
"broil", "flash", "slice", "trunk", "drain", "twist", "track", "flick", "mirth", "storm",
"swirl", "clash", "grape", "spine", "spool", "spike", "plaza", "drift", "creek", "bloom", 
"brisk", "grasp", "trend", "smile", "clash", "grove", "pearl", "lapse", "twirl", "track",
"tramp", "snack", "wrist", "swoop", "flame", "sweep", "flute", "light", "brake", "plaza", 
"grove", "stone", "swoop", "grape", "flock", "spike", "flick", "storm", "vigor", "smile",
"creek", "blaze", "grape", "clash", "flame", "spine", "plumb", "roast", "drift", "brisk", 
"grasp", "track", "slice", "tramp", "flash", "twirl", "flute", "sweep", "grove", "straw",
"brake", "grape", "vigor", "pearl", "swoop", "clash", "trend", "spool", "twist", "flick",
"broil", "flash", "smile", "swoop", "drain", "storm", "track", "tiger", "grasp", "creek", 
"spike", "flick", "flute", "brisk", "swirl", "slice", "spine", "grove", "snack", "wrist",
"tramp", "stone", "track", "spool", "drift", "plaza", "grape", "flash", "flame", "spike",
"swank", "clash", "tiger", "swoop", "track", "grasp", "brisk", "grove", "spine", "vigor","alert", "bison", "candy", "douse", "eagle", "frost", "grape", "haltz", "ivory", "jolly" 
, "lunar", "marsh", "noble", "opals", "piano", "quipy", "rival", "snare", "tooth","abbey", "acids", "actor", "addle", "adore", "agree", "aisle", "alamo", "album", "alert",
"allay", "allow", "aloft", "altar", "amber", "angry", "anime", "apple", "apply", "arena",
"argue", "aside", "atone", "attic", "audio", "audit", "avail", "await", "avoid", "azure",
"babel", "badge", "baker", "balmy", "banal", "basil", "beach", "beads", "beaus", "beaut",
"bezel", "bible", "billy", "blame", "blare", "bless", "bloke", "bloom", "boast", "boils",
"broke", "broth", "brown", "brunt", "bulge", "bunch", "busts", "buyer", "candy", "canal",
"caput", "caste", "catch", "caves", "chalk", "champ", "charm", "cheap", "cheer", "chess",
"chose", "clamp", "clash", "class", "clean", "clear", "clerk", "clime", "cling", "cloak",
"clock", "close", "cloud", "cluck", "crave", "crash", "cream", "creek", "creme", "crown",
"cuffs", "curls", "curse", "dandy", "dance", "darts", "dazed", "death", "decks", "defog",
"delay", "demon", "dense", "depot", "deter", "ditch", "docud", "douse", "dowry", "drain",
"drake", "drink", "drive", "drool", "ducks", "dumpy", "dunes", "duple", "dusty", "dykes",
"eager", "earth", "empty", "enact", "enjoy", "enrol", "enter", "entry", "equip", "erase",
"exact", "exams", "exist", "extra", "fancy", "fence", "feral", "ferry", "fight", "final",
"flame", "flank", "flare", "fluff", "focus", "foray", "form", "forts", "four", "frown",
"froze", "froze", "gears", "gales", "gaunt", "gavel", "gazed", "gems", "genus", "ghost",
"giddy", "given", "glory", "glove", "grasp", "grape", "gravy", "gride", "grove", "gruel",
"guff", "gutsy", "hairs", "harsh", "haste", "heart", "helix", "hitch", "hoist", "honor",
"house", "hover", "hover", "howls", "humor", "ideal", "idols", "impel", "inbox", "index",
"inept", "input", "inter", "intro", "irate", "irony", "items", "jolly", "jumpy", "joint",
"judge", "juice", "jumpy", "kings", "knack", "knee", "knoll", "knot", "knuck", "lapse",
"latch", "leads", "leash", "lemon", "licks", "lodge", "loose", "lore", "louds", "lunch",
"lurk", "lunch", "maize", "macho", "maker", "march", "meaty", "melon", "merit", "mirth",
"moist", "monks", "moody", "moral", "mourn", "mover", "nadir", "nears", "nerdy", "necks",
"nerds", "noise", "oasis", "ocean", "offer", "ombre", "opera", "opine", "order", "orate",
"outer", "ounce", "over", "oxen", "paint", "pause", "peach", "pearl", "pecan", "piano",
"pouch", "price", "prune", "quash", "quart", "quick", "quiet", "quilt", "race", "rally",
"raves", "reach", "relax", "reels", "reins", "remit", "revel", "rider", "ripen", "risky",
"roast", "round", "saber", "scale", "scout", "seize", "serge", "shaky", "sheer", "shove",
"shrub", "shyer", "silly", "sinew", "skate", "sleek", "slink", "smile", "swoop", "sugar",
"tales", "tango", "taste", "tease", "tense", "thorn", "thump", "threw", "tiger", "tight",
"token", "tools", "tramp", "trial", "twist", "ultra", "unity", "upend", "vague", "vapor",
"vigor", "vixen", "vowel", "vulva", "waste", "whale", "wider", "willy", "wiser", "witch",
"woken", "woody", "worse", "yarns", "yatch", "yappy", "yellow", "yikes", "youth", "zoned""aback", "abate", "abide", "abler", "abuse", "actor", "acute", "adage", "added", "adder",
"adieu", "adore", "adorn", "adopt", "adore", "adust", "agape", "agree", "ahead", "alamo",
"album", "alert", "alias", "alike", "alive", "allay", "allow", "allot", "aloft", "alter",
"amber", "amuse", "anger", "angry", "ankle", "apple", "apply", "aptly", "argue", "aside",
"asset", "audit", "avail", "await", "aware", "awash", "bacon", "badge", "baggy", "baker",
"banal", "barge", "basil", "batch", "beach", "beads", "beaus", "beaut", "belly", "below",
"bench", "billy", "binds", "bingo", "blaze", "bless", "blind", "block", "blood", "bluff",
"blunt", "blush", "boney", "booth", "booty", "brake", "brave", "brawn", "bride", "brisk",
"broil", "broth", "brown", "brush", "bunch", "burst", "candy", "canal", "caput", "carve",
"catch", "cause", "chase", "cheer", "chess", "chose", "clamp", "class", "clash", "clean",
"clear", "clerk", "clime", "cling", "cloak", "clock", "close", "cloud", "cluck", "crave",
"crash", "cream", "creek", "creme", "crest", "crisp", "crown", "cuffs", "curls", "curse",
"daisy", "dance", "darts", "death", "decks", "deeps", "defog", "delay", "demon", "dense",
"depot", "deter", "ditch", "douse", "droll", "drain", "drake", "drink", "drive", "drool",
"ducks", "dumpy", "dunes", "duple", "dusty", "dykes", "eager", "earth", "empty", "enact",
"enjoy", "enrol", "enter", "entry", "equip", "erase", "exact", "exams", "exist", "extra",
"fancy", "fence", "feral", "ferry", "fight", "final", "flame", "flank", "flare", "fluff",
"focus", "foray", "form", "forts", "four", "frown", "froze", "gears", "gales", "gaunt",
"gavel", "gazed", "gems", "genus", "ghost", "giddy", "given", "glory", "glove", "grasp",
"grape", "gravy", "gride", "grove", "gruel", "guff", "gutsy", "hairs", "harsh", "haste",
"heart", "helix", "hitch", "hoist", "honor", "house", "hover", "howls", "humor", "ideal",
"idols", "impel", "inbox", "index", "inept", "input", "inter", "intro", "irate", "irony",
"items", "jolly", "jumpy", "joint", "judge", "juice", "jumpy", "kings", "knack", "knee",
"knoll", "knot", "knuck", "lapse", "latch", "leads", "leash", "lemon", "licks", "lodge",
"loose", "lore", "louds", "lunch", "lurk", "lunch", "maize", "macho", "maker", "march",
"meaty", "melon", "merit", "mirth", "moist", "monks", "moody", "moral", "mourn", "mover",
"nadir", "nears", "nerdy", "necks", "nerds", "noise", "oasis", "ocean", "offer", "ombre",
"opera", "opine", "order", "orate", "outer", "ounce", "over", "oxen", "paint", "pause",
"peach", "pearl", "pecan", "piano", "pouch", "price", "prune", "quash", "quart", "quick",
"quiet", "quilt", "race", "rally", "raves", "reach", "relax", "reels", "reins", "remit",
"revel", "rider", "ripen", "risky", "roast", "round", "saber", "scale", "scout", "seize",
"serge", "shaky", "sheer", "shove", "shrub", "shyer", "silly", "sinew", "skate", "sleek",
"slink", "smile", "swoop", "sugar", "tales", "tango", "taste", "tease", "tense", "thorn",
"thump", "threw", "tiger", "tight", "token", "tools", "tramp", "trial", "twist", "ultra",
"unity", "upend", "vague", "vapor", "vigor", "vixen", "vowel", "vulva", "waste", "whale",
"wider", "willy", "wiser", "witch", "woken", "woody", "worse", "yarns", "yatch", "yappy",
"yellow", "yikes", "youth", "zoned", "zesty", "zebra", "zippy", "apple", "sweet", "fluff",
"light", "round", "peace", "flame", "skirt", "brace", "clear", "lapse", "dream", "glory",
"shine", "hover", "blend", "crest", "range", "chime", "tiger", "plant", "grove", "bench",
"music", "stone", "trick", "clash", "beach", "raise", "draft", "jumpy", "douse", "focus",
"grip", "bless", "shock", "level", "boost", "dance", "lunar", "vivid", "ample", "spare",
"scar", "moody", "brave", "mourn", "storm", "gloom", "trump", "trick", "wrest", "spike",
"latch", "fence", "focus", "whale", "lives", "bacon", "cross", "grace", "moist", "slate",
"flare", "pouch", "spike", "trace", "whale", "gears", "phone", "stone", "glove", "flame"]

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
             continue 
     elif u_word[0] == word[2]:
             print(bcolors.WARNING + u_word[0] + bcolors.ENDC)
             continue  
     elif u_word[0] == word[3]:
             print(bcolors.WARNING + u_word[0] + bcolors.ENDC) 
             continue 
     elif u_word[0] == word[4]:
             print(bcolors.WARNING + u_word[0] + bcolors.ENDC)
             continue
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


def