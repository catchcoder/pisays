#!/usr/bin/python3
""" Raspberry PI Says
watch what numbers (1-4) are displayed and
copy the numbers pressing enter after each number

Run with python3
"""
import random
import time

# makesure random is random
random.seed(time.time())


def play_game(high_score):
    """ Loop and get random number 1-4
    """
    play = True
    pi_says = []

    while play:

        pi_says.append(str(random.randint(1, 4)))
        clear_screen()
        print('Playing Round ' + str(len(pi_says)))
        time.sleep(2)
        for button_no in pi_says:
            clear_screen()
            print('*')
            time.sleep(0.3)
            clear_screen()
            print(button_no)
            time.sleep(1)

        clear_screen()
        print('Go')
        for btn in pi_says:
            player_button = str(input())
            if player_button == btn:
                clear_screen()
            else:
                last_round = len(pi_says) - 1
                clear_screen()
                print('You Failed')
                print('You made it to round ' + str(last_round))
                play = False
                if last_round > high_score:
                    return last_round
                time.sleep(3)
                return high_score


def main():
    """ Main game play loop
    """

    high_score = 0

    while True:
        clear_screen()
        print('Highest round: ', str(high_score))
        input('Press a key to continue')
        high_score = play_game(high_score)


def clear_screen():
    """ Clear Screen with 100 carriage returns
    """
    print('\n' * 100)


if __name__ == '__main__':
    main()
