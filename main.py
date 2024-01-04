import random
from enum import Enum


class GameObject(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class YesOrNo(Enum):
    YES = 1
    NO = 0


def generate_rand_obj():  # This function returns a random element of the list.
    objects = [GameObject(1).name, GameObject(2).name, GameObject(3).name]
    random_num = random.randint(0, 2)
    return objects[random_num]


def validate_game_option():  # This function validates user input.
    while True:
        string_input = input('Choose between the words rock, paper or scissors: ').upper()

        if string_input.isalpha():
            if string_input == GameObject(1).name:
                return string_input
            elif string_input == GameObject(2).name:
                return string_input
            elif string_input == GameObject(3).name:
                return string_input
            else:
                print('Please write the exact word')
        else:
            print('Invalid Input!')


def check_winner(user_obj):  # This function compares user's input against the random one.
    rand_obj = generate_rand_obj()
    print(f"Computer's choice: {rand_obj}")

    if user_obj == GameObject(1).name and rand_obj == GameObject(2).name:
        print('The computer has won!')
    elif user_obj == GameObject(2).name and rand_obj == GameObject(1).name:
        print('The player has won!')
    elif user_obj == GameObject(2).name and rand_obj == GameObject(3).name:
        print('The computer has won!')
    elif user_obj == GameObject(3).name and rand_obj == GameObject(2).name:
        print('The player has won!')
    elif user_obj == GameObject(3).name and rand_obj == GameObject(1).name:
        print('The computer has won!')
    elif user_obj == GameObject(1).name and rand_obj == GameObject(3).name:
        print('The player has won!')
    else:
        print('It is a draw!')


def start_game():
    user_option = validate_game_option()
    check_winner(user_option)


def ask_to_continue():  # This function ask user to continue or not after the game ends.
    while True:
        string_input = input('Do you want to continue playing? Please write Yes or No: ').upper()

        if string_input.isalpha():
            if string_input == YesOrNo(1).name:
                start_game()
            elif string_input == YesOrNo(0).name:
                return print('Thanks for playing!')
            else:
                print('Please choose the correct option')
        else:
            print('Invalid Input!')


def main():
    start_game()
    ask_to_continue()


if __name__ == '__main__':
    main()
