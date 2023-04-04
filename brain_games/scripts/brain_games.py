#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import logic_even
from brain_games.scripts.brain_calc import logic_calc
from brain_games.scripts.brain_gcd import logic_gcd
from brain_games.scripts.brain_progression import logic_progression

name = welcome_user()

def main():
    #welcome_user(name)
    logic_even(name)
    logic_calc(name)
    logic_gcd(name)
    logic_progression(name)
    


if __name__ == '__main__':
    main()
   
