import random
import prompt
from brain_games.cli import name 


def logic_calc():
    operators = ["+", "-", "*"]
    counter = 0
    while counter < 3:
        First_number = random.randint(0, 100)
        Second_number = random.randint(0, 100)
        Random_operator = random.choice(operators)
        print("What is the result of the expression?")
        print("Question:", int(First_number), Random_operator, int(Second_number))
        answer = prompt.string("Your answer: ")
        correct_answer = eval(" int(First_number) " + Random_operator + " int(Second_number)")
        if answer == correct_answer:
            print("Correct!")
        else:
            print("'" + str(answer) + "'" + " is wrong answer ;(. Correct answer was " + "'" + str(correct_answer) + "'" + "\nLet's try again, " + name + "!")
            break
        counter += 1
    if counter == 3:
        print("Congratulations, " + name + "!")
        
    
 