# Asking user for their name, Removing whitespace, Capitalize user's name
name = input("What's your full name? ").strip().title()

# Split user's name into first name and last name
name_parts = name.split(" ")

# First name and Last name assighnment
first_name = name_parts[0]
last_name = name_parts[-1]


# Say hello to user
print(f"Hello, {name}")
print(f"So", first_name,"would you like to go into the Forest ('f') or go to the grasslands ('g'). ")
while True:
 try: 
   # Prompting user for the values of x and y
   x = float(input("What's x? "))
   y = float(input("What's y? "))
   
   answer = (x + y)
# Rounds the answer up to 2 digits
   z = round(x + y, 2)

   print(f"x + y = {z:,}")
   break

# Makes sure the user won't mess up the code by typing a letter 
 except ValueError:
    print("Not a number, try again.")