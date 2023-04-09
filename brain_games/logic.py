from brain_games.cli import welcome_user
import random
import prompt


def Answer(user_answer, correct_answer, name):
    IsRight = str(user_answer) == str(correct_answer)
    Break = False
    if IsRight:
        print("Correct!")
    else:
        print("'" + str(user_answer) + "'" + " is wrong answer ;(."
              "Correct answer was "
              + "'" + str(correct_answer) + "'"
              "\nLet's try again, " + name + "!")
        Break = True
    return Break


def logic(Function, article, message):
    name = welcome_user()
    counter = 0
    while counter < 3:
        random_number = random.randint(0, 100)
        print('Answer "yes" if ' + article + ' number is ' + message +
              ',' + ' otherwise answer "no".')
        print('Question:', random_number)
        user_answer = prompt.string("Your answer: ")
        correct_answer = Function(random_number)
        Break = Answer(user_answer, correct_answer, name)
        if Break:
            break
        counter += 1
    if counter == 3:
        print("Congratulations, " + name + "!")
