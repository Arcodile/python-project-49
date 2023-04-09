import random
import prompt
from brain_games.cli import welcome_user
from brain_games.logic import Answer


def logic_even():
    name = welcome_user()
    counter = 0
    while counter < 3:
        random_number = random.randint(0, 100)
        print('Answer "yes" if the number is even, otherwise answer "no".')
        print('Question:', random_number)
        user_answer = prompt.string("Your answer: ")
        if random_number % 2 == 0:
           correct_answer = 'yes'
        else:
            correct_answer = "no"
        Break = Answer(user_answer, correct_answer, name)
        if Break:
            break
        counter += 1
    if counter == 3:
        print("Congratulations, " + name + "!")


if __name__ == '__main__':
    logic_even()
