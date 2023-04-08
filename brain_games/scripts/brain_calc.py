import random
import prompt
from brain_games.cli import welcome_user


def logic_calc():
    name = welcome_user()
    operators = ["+", "-", "*"]
    counter = 0
    while counter < 3:
        First_number = random.randint(0, 100)
        Second_number = random.randint(0, 100)
        Random_operator = random.choice(operators)
        print("What is the result of the expression?")
        print("Question:", int(First_number), Random_operator,
              int(Second_number))
        user_answer = prompt.string("Your answer: ")
        correct_answer = eval(" int(First_number) " + Random_operator
                              + " int(Second_number)")
        if str(user_answer) == str(correct_answer):
            print("Correct!")
        else:
            print("'" + str(user_answer) + "'" + " is wrong answer ;(."
                  "Correct answer was "
                  + "'" + str(correct_answer) + "'"
                  "\nLet's try again, " + name + "!")
            break
        counter += 1
    if counter == 3:
        print("Congratulations, " + name + "!")


if __name__ == '__main__':
    logic_calc()
