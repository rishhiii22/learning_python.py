name = "Rishi" 

# Length of the string is 5

# Negative Length of the string is -5

print(name[0:3]) # Output: Ris

print(name[-4:-1]) # Output: ish

print(name[1:4]) 
print(name[:4]) # is same as print(name[0:4]) 
print(name[1:]) # is same as print(name[1:5])

# Slicing in Python allows you to extract parts of a string using indices.

word = "Amazing"
word[1:4:2] # Output: az

word = "abcdefghijklmnopqrstuvwxyz"
word[1:9:4] # Output: bf

# Strings Functions

name = "Rishi"
print(len(name)) # Output: 5
print(name.endswith("shi")) # Output: True

print(name.startswith("Ri")) # Output: True

print(name.startswith("ri")) # Output: False

print(name.capitalize()) # Output: Rishi

print(name.replace("R", "S")) # Output: Sishi

print(name.find("shi")) # Output: 2

