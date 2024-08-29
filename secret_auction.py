from art import secret_auction
import os


def clear():  # Prints 50 blank lines
    print("\n" * 50)


def highest_bidder(bid_record):
    """
    find the highest bidder, then display him on the screen
    :param bid_record:
    :return: None
    """
    max_bid = 0
    winner_name = ""
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > max_bid:
            max_bid = bid_amount
            winner_name = bidder

    print(f"The winner is: {winner_name} with a bid of ${max_bid}.")


more_bidders = True
print(secret_auction)
print("Welcome to the secret auction program.")
bidders = {}

while more_bidders:

    name = input("What is your name?: ").capitalize()
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")

    if other_bidders == "no":
        more_bidders = False
    clear()

else:
    highest_bidder(bidders)
