import random
import time


def generate_sequence(difficulty):
    difficulty = int(difficulty)
    random_list = range(difficulty)
    for index in random_list:
        index = random.randrange(1, 101)
        print(f"\r{random_list}", end=' ')
        time.sleep(0.7)
        print("\r ")
    return random_list


def get_list_from_user(difficulty):
    user_list = range(difficulty)
    print("please insert numbers in the same amount as the difficulty you chose\n")
    for index in user_list:
        index = input("\n")
    return user_list


def is_list_equal(user_list, random_list):
    if user_list == random_list:
        print("You win\n")
        return True
    else:
        print("You lose\n")
        return False


def play_MemoryGame(difficulty):
    random_list = generate_sequence(difficulty)
    user_list = get_list_from_user(difficulty)
    WinOrLoseCheck = is_list_equal(random_list, user_list)
    if WinOrLoseCheck:
        return True
    else:
        return False
