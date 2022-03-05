import random # It seems I can use random.choice() and give the computer a list of words it can use.


solution = ["i","n","n"] # I need to figure out how to have this be a random word.
word = ["_" for letter in solution]

print("Welcome to hangman.")

greeting = input("Are you ready to play?(y/n) ")
if greeting == "y":
    print(word)
else: print("bye")

wrong_guesses = 0
while word != solution:
    guess = input("pick a letter: ")
    if guess in solution:

        # for i,ele in enumerate(solution):
        #     if i == guess:
        #         word[i] = solution[i] # TypeError: list indices must be integers or slices, not str
        #                                 # that's because i is a letter, not an index
        
        print("correct!")
        if guess == solution[0]: 
            word[0] = solution[0]       # What if I want more letters? Perhaps a for loop and len()?
        if guess == solution[1]:  
            word[1] = solution[1]
        if guess == solution[2]:
            word[2] = solution[2]
        print(word) 

    else:
        print("wrong")
        wrong_guesses += 1

        def the_hanged(wrong_guesses):
            body = {
            1:"head", # maybe I can make it an emoji head...
            2:"head, body",
            3:"head, body, arms",
            4:"head, body, arms, legs"
            }
            return body[wrong_guesses]

        print(f"the hangman is: {the_hanged(wrong_guesses)}. {4 - wrong_guesses} guesses remaining.") # Maybe I could make it say "legs remaining"

    if wrong_guesses == 4: # I wonder if I could give the user a certain number of guesses based on how long the word is...
        print(f"you lose. the word was {solution}.")
        break

if word == solution:
    print("you did it!") # How to make it ask the user if they want to play again and run through the program with a different word?