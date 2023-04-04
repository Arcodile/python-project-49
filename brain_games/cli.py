import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May i have your name? ')
    print('Hello, ' + name + '!')
    return name

    