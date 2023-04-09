from brain_games.logic import Answer,logic


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def isCorrect(random_number):
    if is_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = "no"
    return correct_answer



def logic_prime():
    logic(isCorrect)


if __name__ == '__main__':
    logic_prime()
    