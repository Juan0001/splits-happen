from bowling_score_calculator import BowlingScoreCalculator
import bowling_game
import pandas as pd

def create_data(num):
    """
    Create bowling game data.
    
    Parameters:
    -------
    num: int
        The number of games that are planned to play

    Returns:
    -------
    bowlings: list of lists
        A list of lists with sequence of rolls from one game and its corresponding sore.
    """

    # random.seed(1)  # Initialize for repetitive results when debugging

    bowlings = []
    calculator = BowlingScoreCalculator()
    for i in range(num):
        sequence = bowling_game.one_game()
        rolls = calculator.tokenize_seq(sequence)
        trans_rolls = calculator.transform_symbol(rolls)
        score = calculator.calculate_score(trans_rolls)
        bowling = [sequence, score]
        bowlings.append(bowling)
    
    return bowlings
    
def make_dataframe(bowlings):
    """
    Put the bowling game data into a pandas dataframe.
    
    Parameters:
    -------
    bowlings: list of lists
        A list of lists with sequence of rolls from one game 
        and its corresponding sore.

    Returns:
    -------
    bowlings_df: pandas dataframe
        A pandas dataframe with sequence of rolls from one game 
        and its corresponding sore in each column.
    """
    columns=['Sequence', 'Score']
    bowlings_df = pd.DataFrame(bowlings, columns=columns)
    return bowlings_df

def save_data(bowlings_df, file_path):
    """
    Save the data into a CSV file.
    
    Parameters:
    -------
    bowlings_df: pandas dataframe
        A pandas dataframe with sequence of rolls from one game 
        and its corresponding sore in each column.

    file_path: str
        A path including the name of the file to save the data.
    """
    bowlings_df.to_csv(file_path, index=False, quoting=1)
    

def main(num, file_path):
    """
    Create bowling game data and save it.
    
    Parameters:
    -------
    num: int
        The number of games that are planned to play
        
    file_path: str
        A path including the name of the file to save the data.
    """
    bowlings = create_data(num)
    bowlings_df = make_dataframe(bowlings)
    save_data(bowlings_df, file_path)
    

if __name__== "__main__":
    main(5000, 'bowling_data_5000.csv')
    

