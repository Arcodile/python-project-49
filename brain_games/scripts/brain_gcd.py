import random
import prompt
import math
from brain_games.cli import welcome_user


def logic_gcd():
    name = welcome_user()
    counter = 0
    while counter < 3:
        First_gcd_number = random.randint(0, 100)
        Second_gcd_number = random.randint(0, 100)
        print("Find the greatest common divisor of given numbers.")
        print("Question:", First_gcd_number, Second_gcd_number)
        user_answer = prompt.string("Your answer: ")
        correct_answer = math.gcd(First_gcd_number, Second_gcd_number)
        if str(user_answer) == str(correct_answer):
            print("Correct!")
        else:
            print("'" + str(user_answer) + "'" + " is wrong answer ;(."
                  "Correct answer was " + "'" + str(correct_answer) + "'"
                  "\nLet's try again, " + name + "!")
            break
        counter += 1
    if counter == 3:
        print("Congratulations, " + name + "!")


if __name__ == '__main__':
    logic_gcd()
