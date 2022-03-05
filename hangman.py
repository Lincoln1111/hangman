import random # It seems I can use random.choice() to give the computer a list of words it can use.


solution = ["f","u","n"] # I need to figure out how to have this be a random word.
word = ["_" for letter in solution]

print("welcome to hangman.")

greeting = input("are you ready to play?(y/n) ")
if greeting == "y":
    print(word)
else: print("bye")

def the_hanged(wrong_guesses):
    body = {
    1:"head",
    2:"head + body",
    3:"head + body + arms",
    4:"head + body + arms + legs"
    }
    return body[wrong_guesses]

wrong_guesses = 0
while word != solution:
    guess = input("pick a letter: ")
    if guess in solution:
        print("correct!")
        if guess == "f":
            word[0] = "f"
        if guess == "u":  # I need to figure out how to make this chunk of code apply to any word. maybe a for loop?
            word[1] = "u"
        if guess == "n":
            word[2] = "n"
        print(word) 
    else:
        print("wrong")
        wrong_guesses += 1
        print(f"the hangman is: {the_hanged(wrong_guesses)}. {4 - wrong_guesses} guesses remaining.") # Maybe I could make it say "legs remaining"
    if wrong_guesses == 4: # I wonder if I could give the user a certain number of guesses based on how long the word is...
        print(f"you lose. the word was {solution}.")
        break
if word == solution:
    print("you did it!") # How to make it ask the user if they want to play again and run through the program with a different word?


# This is a good step in the right direction...

# Now I want to figure out how to count the wrong guesses.
    # ok now to correspond wrong guesses to body parts:
    # 1 = head. 
    # 2 = head + body.
    # 3 = head + body + arms.
    # 4 = head + body + arms + legs = game over.


# It's coming along, daggum! I haven't even googled anything yet...
# It's pretty satisfactory so far...

# hmm...I wonder if I can use a list comprehension to make word from solution...let's see...ok got it.