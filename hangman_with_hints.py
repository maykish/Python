#!usr/bin/python3
import random

HANGMANPICS = ["""
        
        +---+
        |   |
            |
            |
            |
            |
    ==========""", """

        +---+
        |   |
        O   |
            |
            |
            |
    ==========""", """

        +---+
        |   |
        O   |
        |   |
            |
            |
    ==========""", """

        +---+
        |   |
        O   |
        |\  |
            |
            |
    ==========""", """

        +---+
        |   |
        O   |
       /|\  |
            |
            |
    ==========""", """

        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
    ==========""", """

        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
    =========="""]

words_and_hints = {"ant":"small", "baby":"young", "badge":"well-deserved", "bat":"halloween", "bear":"dangerous", "beaver":"creek", "camel":"desert", "cat":"feline", "clam":"shell", "cobra":"reptile", "con":"bad thing", "coyote":"wolf", "crow":"bird", "deer":"spotty animal", "dog":"pet", "deck":"cards", "duck":"hunt", "eagle":"bird", "ear":"body part", "error":"computer vocab", "fence":"guard", "fang":"teeth", "fox":"mammal", "frog":"reptile", "fly":"move", "frown":"face", "goat":"milk", "goose":"bird", "gate":"fence", "gland":"body part", "glory":"hero", "hawk":"preys", "hook":"fishing", "ham":"meat", "horn":"sheep", "hoof":"deer", "heat":"temperature", "hive":"bees", "hate":"emotion", "ice":"cold", "igloo":"ice", "item":"thing", "ion":"science", "jaguar":"spotty animal", "joke":"hahaha", "jeans":"clothing", "kite":"sky", "kiss":"love", "lion":"african animal", "lizard":"reptile", "llama":"minecraft animal", "lake":"water", "mole":"body", "monk":"temple", "monkey":"jungle", "moose":"forest", "mouse":"cheese", "mate":"guy", "mule":"horse", "nose":"body", "net":"fishing", "note":"on paper", "ocean":"biome", "owl":"night", "oak":"tree", "panda":"China", "pig":"farm animal", "parrot":"exotic", "pigeon":"bird", "python":"reptile" ,"rabbit":"cute", "rank":"scoring", "rat":"black plague", "raven":"bird", "rhino":"african animal", "ring":"jewelry", "salmon":"fish", "seal":"sea animal", "shark":"scary", "sheep":"minecraft animal", "skunk":"stinky", "sloth":"animal", "snake":"reptile", "spider":"scary", "steak":"meat", "swan":"bird", "tiger":"animal", "toad":"reptile", "tank":"clothes", "top":"clothes", "turkey":"bird", "turtle":"reptile", "whale":"ocean", "wolf":"mammal", "yolk":"cooking", "zebra":"animal"}

def getRandomWord(words):
    random_word = random.choice(list(words.keys()))
    return random_word

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()
    
    print("Hint: " + words_and_hints[secretWord])
    print("============================")

    print("Missed letters:", end=" ")
    for letter in missedLetters:
        print(letter, end=" ")
    print()

    # Blanks and correctly guessed letters
    blanks = "_" * len(secretWord)
    
    # loops through every single letter and slices the word
    # into drawing needed blanks around the guessed letters
    for i in range(len(secretWord)):

        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    print ("word = ", end=" ") 

    for letter in blanks:
        print(letter, end=" ")
    print()
    print()

def getGuess(alreadyGuessed):
    while True:
        print("Guess a letter.")
        guess = input()
        guess = guess.lower()


        if len(guess) != 1:
            print("Please enter a single letter.")

        elif guess in alreadyGuessed:
            print("You have already guessed that letter. Choose again.")

        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a LETTER.")
       
        else:
            return guess

def playAgain():
    print("Do you want to play again? (Yes or no)")
    return input().lower().startswith("y")
   
print("H A N G M A N")
missedLetters = " " 
correctLetters = " "
secretWord = getRandomWord(words_and_hints)
gameIsDone = False

while True:
    displayBoard(
            HANGMANPICS,               
            missedLetters, 
            correctLetters, 
            secretWord
            )

    guess = getGuess(missedLetters + correctLetters)
    
    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
             if secretWord[i] not in correctLetters:
                 foundAllLetters = False
                 break
        if foundAllLetters:
            print(f"Yes! The secret word is \"{secretWord}\"! You won the game!")
            gameIsDone = True

    else:
        missedLetters = missedLetters + guess
    
        # Check if the player has guessed too many times and lost
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(
                    HANGMANPICS, 
                    missedLetters, 
                    correctLetters, 
                    secretWord
                    )
            print(
                f"You have run out of guesses!\n"
                f"After {str(len(missedLetters))} missed guesses and "
                f"{str(len(correctLetters))} correct guesses, "
                f"the word was \"{secretWord}\""
            )
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = " "
            correctLetters = " "
            secretWord = getRandomWord(words_and_hints)
            gameIsDone = False
        else:
            break






















