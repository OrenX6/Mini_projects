import os
import random
from art import logo_blackjack


def clear_screen():
    """
    restart the game
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def calculate_hand_value(hand):
    """
    calculate the value of player hand's cards or dealer hand's cards
    :param hand:
    :return: value
    """
    score = sum(hand)
    if score > 21 and 11 in hand:
        score -= 10
    return score


def hit(hand):
    """
    request an extra card from the dealer put it in your hand
    :param hand:
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # infinite deck
    hand += [random.choice(cards)]


def bust(hand):
    """
    check if player's hand or dealer's hand has a bust
    :param hand:
    :return True or false
    """
    return True if calculate_hand_value(hand) > 21 else False


def is_blackjack(hand):
    """
    check if player's hand or dealer's hand has a blackjack
    :param hand:
    :return: True of False
    """
    return True if calculate_hand_value(hand) == 21 else False


def play_game():
    player_hand = []
    dealer_hand = []
    for _ in range(2):  # deal each player two cards
        hit(player_hand)
        hit(dealer_hand)

    take_another_card = True

    if is_blackjack(player_hand):
        take_another_card = False

    print(logo_blackjack)
    while take_another_card:  # player's hand
        print(f"Your cards: {player_hand}, current score: {calculate_hand_value(player_hand)}")
        print(f"Dealer's first card: {dealer_hand[0]}")
        choice = input("Type 'hit' to get another card, type 'stand' to pass: ")
        if choice == 'hit':
            hit(player_hand)
        if bust(player_hand) or choice == 'stand' or is_blackjack(player_hand):
            take_another_card = False

    while calculate_hand_value(dealer_hand) < 17:  # dealer's hand
        hit(dealer_hand)

    print(f"Your final hand: {player_hand}, final score: {calculate_hand_value(player_hand)}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {calculate_hand_value(dealer_hand)}")

    if bust(player_hand):
        print("You bust ! , dealer win !")
    elif bust(dealer_hand):
        print("dealer bust, You win !")
    elif calculate_hand_value(player_hand) > calculate_hand_value(dealer_hand):
        if is_blackjack(player_hand):
            print("Win with a Blackjack 😎")
        else:
            print("you win !")
    elif calculate_hand_value(player_hand) < calculate_hand_value(dealer_hand):
        if is_blackjack(dealer_hand):
            print("Lose, opponent has Blackjack 😱")
        else:
            print("You lose !")
    else:
        print("Push")


# another game:
while input("Do you want to play a game of BlackJack? type 'y' ot 'n': ").lower() == 'y':
    clear_screen()
    play_game()
