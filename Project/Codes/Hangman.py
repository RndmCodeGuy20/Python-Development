import random
# TODO 1. -> Create a list which contains the words the user will be getting in the game.

wordList = ["condensation","blizzard","disavow","espionage","fjord","glowworm","jaundice","khaki","larynx","mystify","oxidize","numbskull"]

# TODO 2.  -> Randomly Choose a word from the list

chosenWord = random.choice(wordList)

# TODO 3. -> Ask the user to guess a letter and assign their answer to a variable called guessedLetter. Make guess lowercase simultaneously.

guessedLetter = input("Guess a Letter : ").lower()

for letter in chosenWord:
    if letter == guessedLetter:
        print("Right")
    else:
        print("Wrong")