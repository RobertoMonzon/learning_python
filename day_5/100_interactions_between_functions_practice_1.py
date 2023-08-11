# Create a function (roll_dice) that rolls two random dice and returns their results:
# The function must return two result values, which are between 1 and 6).
# Such a function must not require any arguments to function, but must internally generate the random values.
# Provide the result of these two dice to a function called evaluate_play (that is, this second function must receive two arguments) and return -without printing- a message based on the sum of these values:
# If the sum is less than or equal to 6:
# "The sum of your dice is {sum_dice}. Sorry."
# If the sum is greater than 6 and less than 10:
# "The sum of your dice is {sum_dice}. You have a good chance"
# If the sum is greater than or equal to 10:
# "The sum of your dice is {sum_dice}. It looks like a winning move."
# Hints: Use the choice or randint method of the random library to choose a random value between 1 and 6.

import random

def roll_dice():
    die=random.randint(1,6)
    return die


def evaluate_play(die1,die2):
    sum_dice= die1+die2
    if sum_dice <=6:
        return (f"the sum of your dice is {sum_dice}. Sorry.")
    elif sum_dice <6 and sum_dice <10:
        retunr (f"The sum of your dice is {sum_dice}. You have a good chance")
    elif sum_dice >=10:
        return (f"The sum of your dice is {sum_dice}. It looks like a winning move.")

di1=roll_dice()
di2=roll_dice()
evaluate_play(di1,di2)

