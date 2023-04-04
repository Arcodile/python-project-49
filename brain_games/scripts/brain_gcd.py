import random
import prompt
import math
from brain_games.cli import welcome_user


def logic_gcd(name=None):
    if name is None:
        name = welcome_user()
    counter = 0
    while counter < 3:
        First_gcd_number = random.randint(0, 100)
        Second_gcd_number = random.randint(0, 100)
        print("Find the greatest common divisor of given numbers.")
        print("Question:", First_gcd_number, Second_gcd_number)
        answer = prompt.string("Your answer: ")
        correct_gcd = math.gcd(First_gcd_number, Second_gcd_number)
        if str(answer) == str(correct_gcd):
            print("Correct!")
        else:
            print("'" + str(answer) + "'" + " is wrong answer ;(. Correct answer was " + "'" + str(correct_gcd) + "'" + "\nLet's try again, " + name + "!")
            break
        counter += 1
    if counter == 3:
        print("Congratulations, " + name + "!")


if __name__ == '__main__':
    logic_gcd()