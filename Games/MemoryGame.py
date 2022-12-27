import random
import time


def generate_sequence(difficulty):
    difficulty = int(difficulty)
    random_list =list(range(difficulty))

    for index in random_list:
        random_list[index] = random.randrange(1, 101)
        print(f"\r{random_list[index]}", end=' ')
        time.sleep(1)
        print("\r ")
    return random_list


def get_list_from_user(difficulty):
    user_list = list(range(difficulty))
    print("please insert the numbers from first to last and press enter after inserting the number\n")
    for index in user_list:
        user_list[index] = input("\n")
        user_list[index] = int(user_list[index])
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
