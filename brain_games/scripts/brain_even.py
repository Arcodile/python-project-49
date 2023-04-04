import random
import prompt
from brain_games.cli import welcome_user



def logic_even(name=None):
    if name is None:
        name = welcome_user()
    counter = 0
    while counter < 3:
        a = random.randint(0, 100)
        print('Answer "yes" if the number is even, otherwise answer "no".')
        print('Question:', a)
        answer = prompt.string("Your answer: ")
        if a % 2 == 0:
            if answer == "yes":
                print("Correct!")
            else:
                print(answer + " is wrong answer ;(. Correct answer was 'yes' \nLet's try again, " + name + "!")
                break
        else:
            if answer == "no":
                print("Correct!")
            else:
                print(answer + " is wrong answer ;(. Correct answer was 'no' \nLet's try again, " + name + "!")
                break
        counter += 1
    if counter == 3:
        print("Congratulations, " + name + "!") 


if __name__ == '__main__':
 logic_even()