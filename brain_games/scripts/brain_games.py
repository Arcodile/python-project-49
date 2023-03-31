#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import logic_even
from brain_games.scripts.brain_calc import logic_calc
from brain_games.scripts.brain_gcd import logic_gcd


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    logic_even(name)
    logic_calc(name)
    logic_gcd(name)
    


if __name__ == '__main__':
    main()
   
