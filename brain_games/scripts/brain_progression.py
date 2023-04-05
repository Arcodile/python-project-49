import random
import prompt
from brain_games.cli import welcome_user


def print_list(list):
    sentence = ""
    for item in list:
        sentence += str(item) + ' '
    print("Question: " + sentence)


def logic_progression(name=None):
    if name is None:
        name = welcome_user()
    print("What number is missing in the progression?")
    counter = 0
    while counter < 3:
        First_argument = random.randint(0, 10)
        Second_argument = random.randint(30, 100)
        Step_argument = random.randint(2, 10)
        progression = list(range(First_argument, Second_argument,
                                 Step_argument))
        random_index = random.randint(0, len(progression) - 1)
        unknown_element = progression[random_index]
        progression[random_index] = str("..")
        print_list(progression)
        answer = prompt.string("Your answer: ")
        if str(answer) == str(unknown_element):
            print("Correct!")
        else:
            print("'" + str(answer) + "'" + " is wrong answer ;(."
                  "Correct answer was " + "'" + str(unknown_element) + "'"
                  "\nLet's try again, " + name + "!")
            break
        counter += 1
    if counter == 3:
        print("Congratulations, " + name + "!")


if __name__ == '__main__':
    logic_progression()
