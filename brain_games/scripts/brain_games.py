#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import logic_even
from brain_games.scripts.brain_calc import logic_calc



def main():
    print("Welcome to the Brain Games!")
    welcome_user()
    logic_even()
    logic_calc()
    


if __name__ == '__main__':
    main()
   
