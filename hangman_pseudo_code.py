# Alright. The objective here is to build a hangman game.
# How is hangman played?

# In the game one person has a random word in their mind. The other person tries to guess it letter by letter. Simple enough.

# So there's a knower and a guesser. The knower informs the guesser how many letters are in the word. the guesser then guesses a letter.
# If it was correct the knower indicates where the letter stands in the word.
# If it was wrong, the hangman gains a body part.
# This repeats until the guesser completes the word, or the knower completes the hangman--head, body, arm, arm, leg, leg.

# As far as a program is concerned, I'm obviously gonna have to keep this as simple as possible; it probably be played in the terminal,
#   unless I can figure out how to do it using some other way, but we'll start by seeing what can be done in the terminal alone.

# The computer will be the knower. Ther user, the guesser.


# We'll start with the word. This process will be like the guessing game. The computer gets a random word...
# I'd have to specify how long the string will be, or at least how long it can be.

# Then the computer will have to print how many characters the string has; perhaps using underscores and spaces: _ _ _

# The coputer will then prompt a guess from the user. The user will input a single letter.
# If the letter is in the mystery word, the computer will print it: _ u _

# If the letter is not in the mystery word, the computer will begin building the hangman. Perhaps by simply printing the parts in succession.
# like so: head, body, arms, legs. We'll keep it really simple, starting with just up to 3 letter words. and only four guesses.

# When the computer finishes printing head, body, arms, legs, the game is over and the user has lost.
# When the compiter finishes revealing the mystery word the game is over and the user has won.


# I can simplify this down by just giving the computer a word at first. I'd like to keep building upon this project and get it pretty cool.

# The word will probably have to be a list. [_, _, _] then I can alter each letter of the word.

# I can start by making this so basic that the word = ["f", "u", "n"] word[0] = "f" word[1] = "u" and word[2] = "n".

# The computer will display [_, _, _]

# if guess = "f": return ["f", _, _] by changing word[0] from "_" to "f". Same for other letters.
#  else: print(wrong) # We can worry about building the body later.

