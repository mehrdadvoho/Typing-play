# for letter in range(ord('A'), ord('Z') + 1):
#     print(chr(letter), end=' ')

# import keyboard
# from termcolor import colored

# alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# for letter in alphabet:
#     print(colored(letter, 'white'), end=' ')

# print("\nPress any key to change the color to green. Press 'q' to quit.")

# while True:
#     char_pressed = keyboard.read_key()
#     if char_pressed.lower() == 'q':
#         break
#     if char_pressed.upper() in alphabet:
#         index = alphabet.index(char_pressed.upper())
#         alphabet[index] = colored(char_pressed.upper(), 'green')
#         print(' '.join(alphabet))

# import keyboard
# from termcolor import colored
# import string
# import os

# alphabet = list(string.ascii_uppercase)

# for letter in alphabet:
#     print(colored(letter, 'white'), end=' ')


# while True:
#     char_pressed = keyboard.read_key()
#     if char_pressed.lower() == 'q':
#         break
#     if char_pressed.isalpha() and char_pressed.upper() in alphabet:
#         index = alphabet.index(char_pressed.upper())
#         alphabet[index] = colored(char_pressed.upper(), 'green')
#         os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal screen
#         for letter in alphabet:
#             print(colored(letter, 'white' if letter.isupper() else 'green'), end=' ')
#         print("\nPress any key to change the color to green. Press 'q' to quit.")

# import keyboard
# from termcolor import colored
# import string
# import os

# alphabet = list(string.ascii_uppercase)
# original_alphabet = list(string.ascii_uppercase)

# for letter in alphabet:
#     print(colored(letter, 'white'), end=' ')

# print("\nPress any key to change the color to green. Press 'q' to quit.")

# while True:
#     char_pressed = keyboard.read_key()
#     if char_pressed.lower() == 'q':
#         break
#     if char_pressed.isalpha() and char_pressed.upper() in alphabet:
#         index = alphabet.index(char_pressed.upper())
        
#         # Reset previously changed letters to white color
#         for i in range(len(alphabet)):
#             if alphabet[i] != original_alphabet[i]:
#                 alphabet[i] = original_alphabet[i]
        
#         # Change color of the newly pressed letter to green
#         alphabet[index] = colored(char_pressed.upper(), 'green')
        
#         os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal screen
#         for letter in alphabet:
#             print(colored(letter, 'white' if letter.isupper() else 'green'), end=' ')
#         print("\nPress any key to change the color to green. Press 'q' to quit.")



# import keyboard
# from termcolor import colored
# import string
# import os

# alphabet = list(string.ascii_uppercase)
# original_alphabet = list(string.ascii_uppercase)

# for letter in alphabet:
#     print(colored(letter, 'white'), end=' ')

# print("\nPress any key to change the color to green. Press 'q' to quit.")

# while True:
#     char_pressed = keyboard.read_key()
#     if char_pressed.lower() == 'q':
#         break
#     if char_pressed.isalpha() and char_pressed.upper() in alphabet:
#         index = alphabet.index(char_pressed.upper())
        
#         # Reset previously changed letters to white color
#         for i in range(len(alphabet)):
#             if alphabet[i] != original_alphabet[i]:
#                 alphabet[i] = original_alphabet[i]
        
#         # Change color of the newly pressed letter to green
#         alphabet[index] = colored(char_pressed.upper(), 'green')
        
#         os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal screen
        
#         # Print letters A to M on one line
#         print(' '.join(colored(letter, 'white' if letter.isupper() else 'green') for letter in alphabet[:13]))
        
#         # Print letters N to Z on the next line
#         print(' '.join(colored(letter, 'white' if letter.isupper() else 'green') for letter in alphabet[13:]))
        
#         print("\nPress any key to change the color to green. Press 'q' to quit.")


import keyboard
from termcolor import colored
import string
import os

alphabet = list(string.ascii_uppercase)
original_alphabet = list(string.ascii_uppercase)

# Print letters A to M on one line
print(' '.join(colored(letter, 'white') for letter in alphabet[:13]))

# Print letters N to Z on the next line
print(' '.join(colored(letter, 'white') for letter in alphabet[13:]))

print("\nPress any key to change the color to green. Press 'q' to quit.")

while True:
    char_pressed = keyboard.read_key()
    if char_pressed.lower() == 'q':
        break
    if char_pressed.isalpha() and char_pressed.upper() in alphabet:
        index = alphabet.index(char_pressed.upper())
        
        # Reset previously changed letters to white color
        for i in range(len(alphabet)):
            if alphabet[i] != original_alphabet[i]:
                alphabet[i] = original_alphabet[i]
        
        # Change color of the newly pressed letter to green
        alphabet[index] = colored(char_pressed.upper(), 'green')
        
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal screen
        
        # Print letters A to M on one line
        print(' '.join(colored(letter, 'white' if letter.isupper() else 'green') for letter in alphabet[:13]))
        
        # Print letters N to Z on the next line
        print(' '.join(colored(letter, 'white' if letter.isupper() else 'green') for letter in alphabet[13:]))
        
        print("\nPress any key to change the color to green. Press 'q' to quit.")
