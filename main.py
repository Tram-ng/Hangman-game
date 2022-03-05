
## Import Libraries ##
import time, random
from os import system, name

## Import Words From File ##
words = ((open("words.txt", "r")).read()).split("\n")

## Functions ##
def clear():
    '''+
        This function clears CMD
    '''
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

class Game:
    def __init__(self, words):
        self.words_all = words
        self.word = ""
        self.word_format = ""
        self.wrong_letters = ""
        self.left_over = ""
        self.game = True
        self.lifes = 10
        self.correct_guesses = []

    def GameMenu(self):
        clear()
        choice = input("-= + Hangman + =-\n(Enter 1) - Play Game\n(Enter 2) - Exit\n\nInput: ")
        
        if choice == "1": self.GamePlay()
        elif choice == "2": lambda: [clear(), exit()]

    def GameSetup(self):
        self.word = (random.choice(self.words_all)).upper()
        self.word_format = ""
        self.wrong_letters = ""
        self.left_over = list(self.word)
        self.lifes = 10
        self.game = True
        self.correct_guesses = []

        for _ in self.word:
            self.word_format += " _"
    
    def CheckGame(self):
        if self.lifes == 0 or self.left_over == []:
            self.game = False

            if self.left_over == []: 
                clear()
                print(f"You win! The word was {self.word}")

            elif self.lifes == 0:
                clear()
                print(f"GAME OVER! The word was {self.word}")

            input("Press enter to continue...")
            self.GameMenu()

    def GamePlay(self):
        clear()
        self.GameSetup()
        while self.game:
            clear()
            #print(self.word) # Remove comment to enab,le this cheat
            #print(self.left_over) # Remove comment to enable this cheat
            print(f"-= + Hangman + =-\n\nWord: {self.word_format}\n\nWrong Guesses: {self.wrong_letters}\n\nLives Left: {self.lifes}")
            guess = input("Guess: ")

            while len(guess) != 1:
                clear()
                print(f"-= + Hangman + =-\n\nWord: {self.word_format}\nWrong Guesses: {self.wrong_letters}\nLives Left: {self.lifes}")
                guess = input("Only 1 letter per guess! - Guess: ")

            if guess.upper() in self.word:
                if guess.upper() in self.left_over:
                    self.left_over = list(filter(lambda a: a != guess.upper(), self.left_over))
                    self.correct_guesses.append(guess.upper())

                    self.word_format = ""
                    for i in self.word:
                        if i in self.correct_guesses:
                            self.word_format += f" {i}"
                        else:
                            self.word_format += " _"

                else:
                    print("Letter already guessed!")
                    time.sleep(1)

            elif guess.upper() in self.wrong_letters:
                clear()
                print("Letter already guessed!")
                time.sleep(1)
                clear()
            
            else:
                clear()
                self.wrong_letters += f" {guess.upper()}"
                self.lifes -= 1
                print("Incorrect Letter...")
                time.sleep(1)
                clear()

            self.CheckGame()
    


if __name__ == "__main__":
    run = Game(words)
    run.GameMenu()