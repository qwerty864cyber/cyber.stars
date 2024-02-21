import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def smiley_face():
    clear_screen()
    print("""
           .-""""""-.
         .'          '.
        /   O      O   \\
       :           `    :
       |                |   
       :    .------.    :
        \\  '        '  /
         '.          .'
           '-......-'
    """)

def display_text():
    print("\033[1m\033[91mNope wrong file\033[0m")

if __name__ == "__main__":
    smiley_face()
    display_text()
