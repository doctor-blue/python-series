import random


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation = translation+'g'
        else:
            translation += letter
    return translation


def guess_number():
    computer_num = random.randint(1, 100)
    print('I have a number for you! Please guess it ')
    num_of_plays = 0
    max_num_of_plays = 2

    while num_of_plays != max_num_of_plays:
        user_num = int(input("What's your number ?  "))
        turn_left = max_num_of_plays - num_of_plays - 1

        if user_num == computer_num:
            print("You win!!!!")
            break
        elif user_num > computer_num:
            print(
                f"Your number greater than number of computer! \nYou have {turn_left} turn left to guess")
        elif user_num < computer_num:
            print(
                f"Your number less than number of computer! \nYou have {turn_left} turn left to guess")

        num_of_plays += 1
        if(turn_left == 0):
            print("You lose!!! computer_num = ", computer_num)
