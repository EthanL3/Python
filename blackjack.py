import os
import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
money = 1000

def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:
            card = 'J'
        if card == 12:
            card = 'Q'
        if card == 13:
            card = 'K'
        if card == 14:
            card = 'A'
        hand.append(card)
    return hand

def play(money):
    print('Your balance is now ' + str(money))
    again = input('Do you want to play again? (Y/N): ').lower()
    if again == 'y':
        dealer_hand = []
        player_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
        game()
       
    else:
        print('Game is over')
        exit()


def total(hand):
    total = 0
    for card in hand:
        if card == 'J' or card == 'Q' or card == 'K':
            total += 10
        elif card == 'A':
            if total >= 11:
                total += 1
            else:
                total += 11
        else:
            total += int(card)
        
    return total

def hit(hand):
    card = deck.pop()
    if card == 11:
        card = 'J'
    elif card == 12:
        card = 'Q'
    elif card == 13:
        card = 'K'
    elif card == 14:
        card = 'A'
    hand.append(card)
    return hand

def print_results(player_hand, dealer_hand):
    print('The dealer has a ' + str(dealer_hand) + ' for a total of ' + str(total(dealer_hand)))
    print('You have a ' + str(player_hand) + ' for a total of ' + str(total(player_hand)))

def blackjack(player_hand, dealer_hand, bet, money):
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        money += (1.5 * bet)
        print('You got a blackjack!\n')
        play()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        money -= bet
        print('Dealer got a blackjack, you lose')
        play()
    
def score(player_hand, dealer_hand, bet, money):
    if total(player_hand) > 21:
        print_results(player_hand, dealer_hand)
        print ("Sorry. You busted. You lose.\n")
        return money - bet
    elif total(dealer_hand) > 21:
        print_results(player_hand, dealer_hand)
        print ("Dealer busts. You win!\n")
        return money + bet
    elif total(player_hand) < total(dealer_hand):
        print_results(player_hand, dealer_hand)
        print ("Sorry. Your score isn't higher than the dealer. You lose.\n")
        return money - bet
    elif total(player_hand) > total(dealer_hand):
        print_results(player_hand, dealer_hand)
        print ("Congratulations. Your score is higher than the dealer. You win\n")
        return money + bet	



def game():
    choice = 0
    print('Welcome to blackjack')
    print('You start with 1000 dollars, and are allowed to bet any amount')
    print('Your current balance is ' + str(money))
    bet = int(input('Enter a bet size, integers only: '))
    if bet > money:
        bet = int(input('Your bet exceeds your remaining money'))
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    temp = True
    blackjack(player_hand, dealer_hand, bet, money)
    while total(player_hand) <= 21  and temp == True:
        print('The dealer is showing a ' + str(dealer_hand[0]))
        print('You have a ' + str(player_hand) + ' for a total of ' + str(total(player_hand)))
        choice = input('Do you want to hit, stand or quit (H/S/Q): ').lower()
        if choice == 'h':
            hit(player_hand)
        elif choice == 's':
            temp = False
        elif choice == 'q':
            print('Bye')
            exit()
            
    while total(dealer_hand) < 17:
        hit(dealer_hand)
    moneyleft = score(player_hand, dealer_hand, bet, money)
    play(moneyleft)

if __name__ == '__main__':
    game()
                
    




