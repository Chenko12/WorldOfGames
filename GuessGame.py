import random


def generate_number(difficulty):
    difficulty = int(difficulty)
    secret_number = random.randrange(0, difficulty)
    return secret_number


def get_guess_from_user():
    user_number = input("please guess the number\n")
    return int(user_number)


def compare_results(secret_number, user_number):
    if secret_number == user_number:
        print("You win\n")
        return True
    else:
        print("You lose\n")
        return False


def play_GuessGame(difficulty):
    secret_number = generate_number(difficulty)
    user_number = get_guess_from_user()
    WinOrLoseCheck = compare_results(secret_number, user_number)
    if WinOrLoseCheck:
        return True
    else:
        return False
