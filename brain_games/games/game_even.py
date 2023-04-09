from brain_games.logic import logic


def is_even(random_number):
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = "no"
    return correct_answer


def logic_even():
    message = 'Answer "yes" if the number is even, otherwise answer "no".'
    logic(is_even, message)


if __name__ == '__main__':
    logic_even()
