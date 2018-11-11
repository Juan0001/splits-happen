##########################################################################
# Program to mimic playing the American Ten-Pin Bowling game and to 
# generate a sequence of roll to record the result of the game.
#
# Author:  Juan L. Kehoe
# Email: juanluo2008@gmail.com
###########################################################################

###########################################################################
# imports
###########################################################################

import random

class BowlingGame:
    def __init__(self):
        pass
    
    def _strike(self):
        return 'X'

    def _spare(self):
        frame_1 = random.randint(0,9)
        if frame_1 == 0:
            scores = '-' + '/'
        else:
            scores = str(frame_1) + '/'
        return scores

    def _none(self):
        frame_1 = random.randint(0,9)
        frame_2 = random.randint(0,9)
        total = frame_1 + frame_2

        if total > 9:
            frame_2 = str(random.randint(0,9))
        elif frame_1 == 0:
            scores = '-' + str(frame_2)
        elif frame_2 == 0:
            scores = str(frame_1) + '-'

        return scores

    def play(self):
        score_type = random.randint(0,1)
        if score_type == 0:
            return self._strike()
        elif score_type == 1:
            return self._spare()
        else:
            return self._none()

    def bonus(self):
        score_type = random.randint(0,1)
        if score_type == 0:
            roll_1 = str(random.randint(0,10))
            roll_2 = str(random.randint(0,10))

            if roll_1 == 10:
                roll_1 = 'X'
            elif roll_1 == 0:
                roll_1 = '-'

            if roll_2 == 10:
                roll_2 = 'X'
            elif roll_2 == 0:
                roll_2 = '-'

            total_score = self._strike() + roll_1 + roll_2

        elif score_type == 1:
            roll = str(random.randint(0,10))
            total_score = self._spare() + roll
        else:
            total_score = self._none()

        return total_score

def one_game():
    bowling = BowlingGame()
    roll_sequence = []
    for i in range(9):
        roll_sequence.append(bowling.play())
    roll_sequence.append(bowling.bonus())

    return ''.join(roll_sequence)

def main():
    print(one_game())

if __name__== "__main__":
    main()
