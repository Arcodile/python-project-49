import random
import prompt
from brain_games.cli import name 


def logic_calc():
    operators = ['+', '-', '*']
    counter = 0
    while counter < 3:
        First_number = random.randint(0, 100)
        Second_number = random.randint(0, 100)
        Random_operator = random.choice(operators)
        print("What is the result of the expression?")
        print("Question:", First_number, Random_operator, Second_number)
        correct_answer = eval(First_number, Random_operator, Second_number)
        answer = prompt.string("Your answer: ")
        if answer == correct_answer:
            print("Correct!")
        else:
            print(answer + " is wrong answer ;(. Correct answer was " + correct_answer + "\nLets's try again, " + name + "!")
            break
        counter += 1
    if counter == 3:
        print("Congratulations, " + name + "!")
        
    
