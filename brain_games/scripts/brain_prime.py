import random
import prompt
from brain_games.cli import welcome_user


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
        a = random.randint(0, 100)
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        print('Question:', a)
        answer = prompt.string("Your answer: ")
        if is_prime(a):
            if answer == "yes":
                print("Correct!")
            else:
                print(answer + " is wrong answer ;(. Correct answer was 'yes'"
                      "\nLet's try again, " + name + "!")
                break
        else:
            if answer == "no":
                print("Correct!")
            else:
                print(answer + " is wrong answer ;(. Correct answer was 'no'"
                      "\nLet's try again, " + name + "!")
                break
        counter += 1
    if counter == 3:
        print("Congratulations, " + name + "!")


if __name__ == '__main__':
    logic_prime()
