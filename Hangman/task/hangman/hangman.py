import random
import sys


def choose():
    answer = input('Type "play" to play the game, "exit" to quit: ')
    while not answer == "play" and not answer == "exit":
        answer = input('Type "play" to play the game, "exit" to quit: ')
    if answer == "play":
        game()
    elif answer == "exit":
        sys.exit()


def game():
    words = ['python', 'java', 'kotlin', 'javascript']
    right_answer = random.choice(words)
    chars = set(right_answer)
    guess = "-" * len(right_answer)
    lifes = 8
    win = False
    inputs = set()
    while lifes > 0:
        if win:
            break
        print()
        print(guess)
        letter = input("Input a letter: ")
        if len(letter) == 1:
            if letter.isascii() and letter.islower():
                if letter not in inputs:
                    inputs.add(letter)
                    if letter in chars:
                        for i in range(len(right_answer)):
                            if right_answer[i] == letter:
                                if guess[i] == "-":
                                    guess = guess[0:i] + letter + guess[i + 1:len(guess)]
                                if '-' not in guess:
                                    print()
                                    print(guess)
                                    print("You guessed the word!")
                                    print("You survived!")
                                    win = True
                                    break
                    else:
                        # print("That letter doesn't appear in the word")
                        print("No such letter in the word")
                        lifes -= 1
                else:
                    # print("You've already guessed this letter")
                    print("You already typed this letter")
            else:
                # print("Please enter a lowercase English letter")
                print("It is not an ASCII lowercase letter")
        else:
            print("You should input a single letter")
    else:
        print("You lost!")
    print()
    choose()


print("H A N G M A N")
choose()
