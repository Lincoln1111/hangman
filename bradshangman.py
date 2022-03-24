from bradsgame import Game

def prompt_to_play(again=False):
    ans = input(f"Wanna play {'again' if again else 'Hangman'}?: ")
    return ans.lower().startswith("n") is False


if prompt_to_play():
    continue_playing = True
    while continue_playing:
        game = Game()
        game.play()
        continue_playing = prompt_to_play(again=True)
print("Come again!")