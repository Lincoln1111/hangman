import os
import random

from words import potential_solutions


class Game():
    def __init__(self):
        self.solution = random.choice(potential_solutions)
        self.clear_screen()
        self.correct_letters = set(self.solution)
        self.guessed_letters = set()
        self.max_incorrect_guesses = 4

    def get_current_hint(self):
        hint = ''.join(
            c if c in self.guessed_letters else '_'
            for c in self.solution
        )
        return hint

    def prompt_for_guess(self):
        while True:
            guess = input("Guess a letter: ")
            if guess in self.guessed_letters:
                print(f"You already guessed {guess}")
            elif guess.isalpha() and len(guess) == 1:
                return guess.lower()
            else:
                print("Invalid guess.")

    def play(self):
        game_over = False
        print(f"You may begin, there are {len(self.solution)} letters:")
        while not game_over:
            self.display_game()
            guess = self.prompt_for_guess()
            self.clear_screen()
            self.guessed_letters.add(guess)
            if guess in self.correct_letters:
                print("Correct!")
                if self.correct_letters.issubset(self.guessed_letters):
                    print("You WIN the game!")
                    game_over = True
                    self.display_game()
            else:
                print("Incorrect!")
                incorrect_letters = self.guessed_letters - self.correct_letters
                if len(incorrect_letters) >= self.max_incorrect_guesses:
                    print("You LOSE the game!")
                    game_over = True
                    self.display_game()
                    print(f"The word was: {self.solution}")

    def display_game(self):
        self.display_hanged()
        print(f"The word: {self.get_current_hint()}")
        incorrect_letters = self.guessed_letters - self.correct_letters
        previous_guesses = ', '.join(sorted(incorrect_letters))
        if previous_guesses:
            print(f"Previous guesses: {previous_guesses}")
        remaining_guesses = self.max_incorrect_guesses - len(incorrect_letters)
        print(f"You have {remaining_guesses} guesses left.")

    def clear_screen(self):
        command = 'cls'
        if os.name == 'posix':
            command = 'clear'
        os.system(command)

    def display_hanged(self):
        state = len(self.guessed_letters - self.correct_letters)
        head = " O " if state > 0 else ""
        arms = "/|\\" if state > 1 else ""
        body = " | " if state > 2 else ""
        legs = "/ \\" if state > 3 else ""
        print("_______")
        print(f" ||  {head}")
        print(f" ||  {arms}")
        print(f" ||  {body}")
        print(f" ||  {legs}")
        print("_||_")
        