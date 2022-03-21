from random import choice
from words import potential_solutions

solution = list(choice(potential_solutions))
word = ["_" for letter in solution]

print("Welcome to hangman.")

greeting = input("Are you ready to play?(y/n) ")
if greeting == "y":
    print(" ".join(word))
else: print("bye"); exit()

wrong_guesses = 0
incorrect_guesses = []
while word != solution:
    guess = input("pick a letter: ")

    i = 0
    while guess in solution and i < len(solution):
        if guess == solution[i]:
            word[i] = guess
        i += 1
    print(" ".join(word))

    if guess not in solution:
        print("WRONG.")
        wrong_guesses += 1
 
        incorrect_guesses.append(guess)
        print(f"You've guessed: {incorrect_guesses}")

        def the_hanged(wrong_guesses):
            body = {
            1:"head",
            2:"head, body",
            3:"head, body, arms",
            4:"head, body, arms, legs"
            }
            return body[wrong_guesses]

        print(f"The hangman is: {the_hanged(wrong_guesses)}. {4 - wrong_guesses} guesses remaining.") 

    if wrong_guesses == 4: # I wonder if I could give the user a certain number of guesses based on how long the word is...
        print(f"You lose. the word was \"{''.join(solution)}.\"")
        break

if word == solution:
    print("you did it!") # How to make it ask the user if they want to play again and run through the program with a different word?