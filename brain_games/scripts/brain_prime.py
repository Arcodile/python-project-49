import random
import prompt
from brain_games.cli import welcome_user
from brain_games.logic import Answer


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def logic_prime():
    name = welcome_user()
    counter = 0
    while counter < 3:
        random_number = random.randint(0, 100)
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        print('Question:', random_number)
        user_answer = prompt.string("Your answer: ")
        if is_prime(random_number):
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
    logic_prime()
    