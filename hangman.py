import random # It seems I can use random.choice() and give the computer a list of words it can use.


solution = ["h","i","s","s"] # I need to figure out how to have this be a random word.
word = ["_" for letter in solution]

print("Welcome to hangman.")

greeting = input("Are you ready to play?(y/n) ")
if greeting == "y":
    print(word)
else: print("bye") # The program still runs after this point...

wrong_guesses = 0
while word != solution:
    guess = input("pick a letter: ")

    i = 0
    while guess in solution and i < len(solution):
        if guess == solution[i]:
            word[i] = guess
        i += 1
    print(word)

    if guess not in solution:
        print("wrong")
        wrong_guesses += 1

        def the_hanged(wrong_guesses):
            body = {
            1:"head",
            2:"head, body",
            3:"head, body, arms",
            4:"head, body, arms, legs"
            }
            return body[wrong_guesses]

        print(f"the hangman is: {the_hanged(wrong_guesses)}. {4 - wrong_guesses} guesses remaining.") 

    if wrong_guesses == 4: # I wonder if I could give the user a certain number of guesses based on how long the word is...
        print(f"you lose. the word was {solution}.")
        break

if word == solution:
    print("you did it!") # How to make it ask the user if they want to play again and run through the program with a different word?