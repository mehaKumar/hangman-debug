import time
import random
NUM_LIVES = 6
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
WORDS_FILENAME = "words.txt"
HANGMEN = {
        0: [
            " +----+ ",
            " |/   | ",
            " |      ",
            " |      ",
            " |      ",
            " |      ",
            "========",
        ],
        1: [
            " +----+ ",
            " |/   | ",
            " |    O ",
            " |      ",
            " |      ",
            " |      ",
            "========",
        ],
        2: [
            " +----+ ",
            " |/   | ",
            " |    O ",
            " |    | ",
            " |      ",
            " |      ",
            "========",
        ],
        3: [
            " +----+ ",
            " |/   | ",
            " |    O ",
            " |   /| ",
            " |      ",
            " |      ",
            "========",
        ],
        4: [
            " +----+ ",
            " |/   | ",
            " |    O ",
            " |   /|\\ ",
            " |      ",
            " |      ",
            "========",
        ],
        5: [
            " +----+ ",
            " |/   | ",
            " |    O ",
            " |   /|\\ ",
            " |   /  ",
            " |      ",
            "========",
        ],
        6: [
            " +----+ ",
            " |/   | ",
            " |    O ",
            " |   /|\\ ",
            " |   / \\ ",
            " |      ",
            "========",
        ],
    }

def getWord():
    fileHandle = open(WORDS_FILENAME, "r")
    words = []
    for line in fileHandle:
        currword = line
        words.append(currword)
    return random.choice(words)

def printHangman(lives):
    idx = NUM_LIVES - lives
    hangman = HANGMEN[idx]
    print("\n".join(hangman))

def insertSpaces(string):
    out = ""
    for character in string:
        out += character + " "
    return out[:-1]

def printWordWithGuesses(word, guesses):
    blanks = ""
    for letter in word:
        if letter in guesses:
            blanks += letter
        else:
            blanks += "_"
    print(insertSpaces(blanks))

def getGuess(listOfGuesses):
    guess = input("Guess a letter! ")
    while ((guess.lower() not in ALPHABET) and 
            (guess.lower() in listOfGuesses)):
        guess = input("Invalid guess, try again: ")
    return guess

def isInWord(letter, word):
    for character in word:
        if letter == character:
            return True
    return False

def checkIfWon(listOfGuesses, secretWord):
    won = True
    for letter in secretWord:
        won = (letter in listOfGuesses) & won
    return won

def printYouWonMessage(word):
    print(insertSpaces(word))
    print("You win, well done!")

def printYouLostMessage(word):
    print("\n".join(HANGMEN[NUM_LIVES]))
    print("YOU LOSE")
    print("The word was: " + insertSpaces(word))

def yesOrNo(string):
    if string[0].lower == "y":
        return True
    return False

def main():
    playing = True
    while (playing):
        print("Let's play Hangman!")
        time.sleep(1)

        word = getWord()
        lives_left = NUM_LIVES
        guesses = ""
        won = False
        
        while lives_left > 0 and not won:
            printHangman(lives_left)
            printWordWithGuesses(word, guesses)
            print()
            curr_guess = getGuess(guesses)
            guesses += curr_guess
            log = isInWord(curr_guess, word)
            if log:
                print("Good guess, that's in the word!")
                won = checkIfWon(guesses, word)
            else:
                print("Sorry, that's not in the word.")
                lives_left -= 1
            time.sleep(1)

        if lives_left > 0:
            printYouWonMessage(word)
        else:
            printYouLostMessage(word)
        playing = yesOrNo(input("Want to play again? (Y or N)"))
    

if __name__ == "__main__":
    main()

