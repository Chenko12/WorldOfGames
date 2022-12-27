from forex_python.converter import CurrencyRates
import random

number = random.randrange(1, 100)


def get_money_interval(difficulty, amount_of_ils):
    c = CurrencyRates()
    usd = (1 / c.convert('ILS', 'USD', amount_of_ils))
    rang = (usd - (5 - difficulty), usd + (5 - difficulty))
    return rang


def get_guess_from_user():
    user_guess = input(f"please guess how much is {number} NIS in USD currency\n")
    return float(user_guess)


def play_cr(difficulty):
    user_guess = get_guess_from_user()
    range_to_win = get_money_interval(difficulty, number)
    if user_guess in range_to_win:
        print("You win")
        return True
    else:
        print("You lose")
        return False
