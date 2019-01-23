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
    """
    To mimic playing the American Ten-Pin Bowling game.
    """

    def __init__(self):
        pass

    @staticmethod
    def _strike():
        """
        A strike roll, marked as 'X'.

        Returns:
        -------
        'X': str
        """
        return 'X'

    def _spare(self):
        """
        A spare roll, marked as '/'. The spare roll usually comes
        in the second roll of a turn.

        And the two rolls together add up to 10.

        Returns:
        -------
        scores: str
            This is a two character string to record the score of the play.
        """
        frame_1 = random.randint(0, 9)
        if frame_1 == 0:
            scores = '-' + '/'
        else:
            scores = str(frame_1) + '/'
        return scores

    def _none(self):
        """
        A roll that is neither strike nor spare.
        And the two rolls together should be less than 10.

        Returns:
        -------
        scores: str
            This is a two character string to record the score of the play.
        """
        frame_1 = random.randint(0, 9)
        frame_2 = random.randint(0, 9 - frame_1)  # the 2nd roll has a maximum of 9 minus first roll

        if frame_1 == 0:
            scores = '-' + str(frame_2)
        elif frame_2 == 0:
            scores = str(frame_1) + '-'
        else:
            scores = str(frame_1) + str(frame_2)

        return scores

    def play(self):
        """
        Play one roll of game.

        Returns:
        -------
        _strike(): function
            If it's a strike.

        _strike(): function
            If it's a spare.

        _none(): function
            If it's neither strike nor spare.
        """
        score_type = random.choice(['strike', 'spare', 'normal'])
        if score_type == 'strike':
            return self._strike()
        elif score_type == 'spare':
            return self._spare()
        else:
            return self._none()

    def bonus(self):
        """
        In the 10th turn, if it's a strike, the player can add another two rolls in;
        if it's a spare, the player can add another one roll; otherwise no more roll.

        Returns:
        -------
        total_score: str
            This is a two or three character string to record the score of the
            last play.
        """
        score_type = random.choice(['strike', 'spare', 'normal'])
        if score_type == 'strike':
            roll_1 = random.randint(0, 10)

            if roll_1 != 10:
                roll_2 = random.randint(0, 10 - roll_1)
                roll_2 = self.transform(str(roll_2))
                roll_1 = self.transform(str(roll_1))
                total_score = self._strike() + roll_1 + roll_2
            else:
                roll_1 = self.transform(str(roll_1))
                total_score = self._strike() + roll_1

        elif score_type == 'spare':
            roll = str(random.randint(0, 10))
            roll = self.transform(roll)
            total_score = self._spare() + roll

        else:
            total_score = self._none()

        return total_score

    def transform(self, roll):
        if roll == '10':
            roll = self._strike()
        elif roll == '0':
            roll = '-'
        return roll


def one_game():
    """
    To play one game which include 10 turns and 2 or 1 bonus rolls depend on a
    strike or spare.

    Returns:
    -------
    roll_sequence: str
        The sequence of rolls from one game.
    """
    bowling = BowlingGame()
    roll_sequence = []
    for i in range(9):
        roll_sequence.append(bowling.play())
    roll_sequence.append(bowling.bonus())

    return ''.join(roll_sequence)


def main():
    print(one_game())


if __name__ == "__main__":
    main()
