from time import sleep
import os
import random
from stages_hangman import stages
print("WELCOME TO THE GAME ")
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')
sleep(2)
os.system("cls")

print('''
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.                 
| |/         |/  _  \                 
| |          ||  `/,|               
| |          (\\`_.'                
| |         .-`--'.                 
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .''')


sleep(2)
os.system("cls")
word_list = ["mouse", "telephone" , "butcher", "abruptly", "blizard", "jaywalk", "croquet", "curacao", " foxglove", "gnostic", " galvanize", "numbskull", "mnemonic","bamboo","pneumonia", "pshaw", "xylophone", "zigzagging", "grogginess" ]

chosen_word = random.choice(word_list)
print(chosen_word)
display = []
word_length = int(len(chosen_word))
for letter in chosen_word:
     display.append("_")
print("The word is:")
print(f"{' '.join(display)}")
number_of_times_guess = 0
wrong =0
while (wrong <= 6) or (not "_" in display):
    guess_letter = input("Guess a letter:").lower()
    number_of_times_guess = number_of_times_guess +1
    if guess_letter in chosen_word:
        for index in range(0, len(chosen_word)):
            letter = chosen_word[index]
            if letter == guess_letter:
                if display[index] != "_":
                    print("You have already guessed this letter")
                display[index] = letter
        print(f"{' '.join(display)}")
        if not "_" in display:
            print(f"The word is : {chosen_word}")
            print("You win")
    else:
        print(f"The letter {guess_letter} is not in thw word")
        print(stages[wrong])
        wrong = wrong +1
    if wrong == word_length and ("_" in display):
        print("YOU LOSE")
        print(f"The word was : {chosen_word}")




