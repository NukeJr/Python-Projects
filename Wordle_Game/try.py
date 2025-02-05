import os 

folder_path = os.path.dirname(__file__)
file_name = os.path.join(folder_path, 'fiveLetterWords.txt')
file = open(file_name)
print(file.read())

print(folder_path)