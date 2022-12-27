from ScoresDirectory import Score
from Games import CurrencyRouletteGame, GuessGame, MemoryGame


def playAgain(restart):
    if restart == "yes":
        load_game()
    else:
        print("Thank you for playing")


def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")
    return ""


def load_game():
    check = False
    while not check:
        game_input = input('''Please choose a game to play by insert number from 1 to 3:\n
                           1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n
                           2. Guess Game - guess a number and see if you chose like the computer\n
                           3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n''')
        game_input = int(game_input)
        if game_input != 1 and game_input != 2 and game_input != 3:
            print("number is invalid! please insert valid number!")
        else:
            check = True

    check = False
    while not check:
        difficulty = input("Please choose game difficulty from 1 to 5:\n")
        difficulty = int(difficulty)
        if difficulty != 1 and difficulty != 2 and difficulty != 3 and difficulty != 4 and difficulty != 5:
            print("number is invalid! please insert valid number!")
        else:
            check = True

        if game_input == 1:
            Win_Or_Lose = MemoryGame.play_MemoryGame(difficulty)
        elif game_input == 2:
            Win_Or_Lose = GuessGame.play_GuessGame(difficulty)
        elif game_input == 3:
            Win_Or_Lose = CurrencyRouletteGame.play_cr(difficulty)
    if Win_Or_Lose:
       Score.add_score(difficulty)

    playAgain(input('''Do you want to play again?\n "
             please insert : (yes/no)'''))
