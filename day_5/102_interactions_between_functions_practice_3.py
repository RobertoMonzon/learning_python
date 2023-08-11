# Create a function (called toss_coin) that returns the result of a (random) coin toss. Such a function must be able to return the results "Heads" or "Tails", and must not receive any arguments to function.
# Create a second function (called test_luck), which takes two arguments: the first must be the result of the coin toss. The second argument will be any list of numbers (you must create a list with values and call it list_numbers).
# If given a "Head", it should display the message to the user: "The list will self-destruct", and remove it (return it as empty list[]).
# If you are given a "Tail", it should print to the screen: "The list was saved" and return the list intact.
# Tracks: Uses the random library's choice method to pick an element at random from a sequence.

import random

list_numbers=[1,2,3,4,5,6]

def toss_coin():
    coin=["Head","Tail"]
    choice_coin=random.choice(coin)
    return choice_coin

def test_luck(coin,list_):
    if coin == "Tail":
        list_.clear()
        return (f"The list will self-destruct {list_}")
    elif coin == "Head":
        return (f"The list was saved {list_}")
    



coin=toss_coin()
print(test_luck(coin,list_numbers))