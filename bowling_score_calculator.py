##########################################################################
# Program to calculate the score for American Ten-Pin Bowling 
# from a sequence of rolls.
#
# Author:  Juan L. Kehoe
# Email: juanluo2008@gmail.com
###########################################################################

def get_sequence():
    """
    To get the roll sequence the input by users from console.

    Returns:
    -------
    seq: str
        A string of rolls in the sequence input by the users.
    """
    seq = input()
    return seq

def tokenize_seq(seq):
    """
    To tokenize the sequence of rolls input from user to single letters.

    Returns:
    -------
    rolls: list
        A list of rolls in the sequence input by the users.
    """
    rolls = [roll for roll in seq]
    return rolls


def transform_symbol(rolls):
    """
    Transform the rolls to scores based on the annotation of the symbols.
    Annotation of the symbols:
        "X" indicates a strike, "/" indicates a spare, "-" indicates a miss, 
        and a number indicates the number of pins knocked down in the roll.

    For symbols:
        'X' -> 10
        '-' -> 0
        '/' -> '/' This will be kept the same to differentiate spare from strike.
    For numbers:
        Will transform the number in str to int.

    Parameters:
    -------
    rolls: list of str
        The rolls in a list that is retrieved from the console.
    
    Returns:
    -------
    rolls: list of str and int
        A list of transformed rolls.
        
    """
    for i in range(len(rolls)):
        # If it's 'X', it's strike. Set the score to 10.
        if rolls[i] == 'X':
            rolls[i] = 10
        # If it's '-', it's missed. Set the score to 0.
        elif rolls[i] == '-':
            rolls[i] = 0
        # If it's '/', it's spare, keep it for the record.
        elif rolls[i] == '/':
            rolls[i] == '/'
        else:
            rolls[i] = int(rolls[i])
    return rolls

def calculate_score(trans_rolls):
    """
    Use the transformed rolls to calculate the score 
    based on the sequence of rolls input by the user from console 
    using the following scoring logic:
        1. Each game, or "line" of bowling, includes ten turns, or "frames" for the bowler.
        2. In each frame, the bowler gets up to two tries to knock down all the pins.
        3. If in two tries, he fails to knock them all down, his score for that frame is the total number of pins knocked down in his two tries.
        4. If in two tries he knocks them all down, this is called a "spare" and his score for the frame is ten plus the number of pins knocked down on his next throw (in his next turn).
        5. If on his first try in the frame he knocks down all the pins, this is called a "strike". His turn is over, and his score for the frame is ten plus the simple total of the pins knocked down in his next two rolls.
        6. If he gets a spare or strike in the last (tenth) frame, the bowler gets to throw one or two more bonus balls, respectively. These bonus throws are taken as part of the same turn. If the bonus throws knock down all the pins, the process does not repeat: the bonus throws are only used to calculate the score of the final frame.
        7. The game score is the total of all frame scores.

    Parameters:
    -------
    trans_rolls: list of str and int
        The rolls in a list that is transformed to have the scores for each roll.
    
    Returns:
    -------
    score: int
        The score of the roll sequence for one line of American Ten-Pin Bowling.
    """
    # set the start score to 0
    score = 0
    # get the total length of the rolls
    l = len(trans_rolls)
    r = trans_rolls
    for i in range(l):
        # check if it's the third roll from backwards
        if i < l - 3:
            # check if it's strike
            if r[i] == 10:
                # if its strike, add current score and score in next two rolls
                # check if there's a spare in the next two rolls
                if r[i+2] == '/':
                    # if it's spare the score for the next two rolls will be 10
                    score += r[i] + 10
                else:
                    score += r[i] + r[i+1] + r[i+2]
            # check if it's spare
            elif r[i] == '/':
                # if it's spare, add current score and score in next one roll
                score += (10 - r[i-1]) + r[i+1]
            else:
                # if its neither strike nor spare, just add the current score
                score += r[i]
        elif i == l - 3:
            # check if the last turn is a spare
            if r[i+1] == '/':
                # if it's a spare, add 10 to the last score  
                score += 10 + r[i+2]
            # check if the second last is a spare
            elif r[i] == '/':
                # if it's a spare, add the next roll, and add the last two rolls
                score += (10-r[i-1]) + r[i+1] + r[i+1] + r[i+2]
            else:
                # if it's not a spare, just add all the scores
                score += r[i] + r[i+1] + r[i+2]
                
    return score

def main():
    """
    To calculate the total score for a American Ten-Pin Bowling game 
    based on the roll seuences input by users from console.

    Some of the sample inputs are as follows:
    |------------------------|----------|
    | Program Input          | Score    |
    |------------------------|----------|
    | XXXXXXXXXXXX           | 300      |
    | 9-9-9-9-9-9-9-9-9-9-   | 90       |
    | 5/5/5/5/5/5/5/5/5/5/5  | 150      |
    | X7/9-X-88/-6XXX81      | 167      |
    |------------------------|----------|

    To run the program:
        python bowling_score_calculator.py
    
    To stop the program:
        Ctrl + c
    """
    while True:
        print("Please input the sequence of rolls: ")
        seq = get_sequence()
        rolls = tokenize_seq(seq)
        trans_rolls = transform_symbol(rolls)
        print("The score for this game is: ")
        print(calculate_score(trans_rolls))


if __name__== "__main__":
    main()
    