from Chips import Chips
from Deck import Deck
from Hand import Hand

def initGame(cardDeck, player, dealer):
    global playing 
    
    player.add_card(cardDeck.deal())
    player.add_card(cardDeck.deal())
    dealer.add_card(cardDeck.deal())
    dealer.add_card(cardDeck.deal())
    cardDeck.shuffle()
    
    playing = True

def placeBet(chips):
    while True:
        print(f"Current amount of chips: {chips.total}")
        try:
            bet = int(input("Place your bet: " ))
        except ValueError:
            print("Your input wasn't valid. Please enter a valid bet!")
        else: 
            if (bet <= chips.total) :
                print("Bet Accepted")
                return bet
            else: print("You bet more than you have. Please try again!")
    
def playerWins(chips):
    chips.win_bet()
    print("THE PLAYER WINS!!")

def playerBusts(chips):
    chips.lose_bet()
    print(f"OH NO PLAYER WENT BUST! DEALER WINS")

def dealerWins(chips):
    chips.lose_bet()
    print("THE DEALER WINS!!!")

def dealerBust(chips):
    chips.win_bet()
    print("YAY! THE DEALER WENT BUST! PLAYER WINS")

def push():
    print('Dealer and player tie! PUSH')

def hit(hand, cardDeck):
    hand.add_card(cardDeck.deal())
    hand.adjust_for_ace()

def hitOrStand(player, cardDeck):
    global playing
    while True:
        choice = input("Would you like to hit or stand? H for hit and S for stand.").lower()
        if(choice == 'h' ):
            hit(player, cardDeck)
            break
        elif(choice == 's'):
            playing = False
            break
        else:
            print("That was not a valid choice. Please try again")


def showSome(player, dealer):
    print("PLAYERS CARDS:")
    for card in player.cards:
        print(card)
    print(f"Current Player Hand Value: {player.value}")

    print("DEALERS CARDS:")
    for card in range(0, len(dealer.cards) - 1):
        print(dealer.cards[card])
    print(f"Current Dealer Hand Value: {dealer.value - dealer.cards[-1].value}")

def showAll(player, dealer):
    dealerSum = 0
    playerSum = 0
    print("PLAYERS CARDS:")
    for card in player.cards:
        playerSum += card.value
        player.value = playerSum
        print(card)
    print(f"Current Player Hand Value: {player.value}")
    print("DEALERS CARDS:")
    for card in dealer.cards:
        dealerSum += card.value
        dealer.value = dealerSum
        print(card)
    print(f"Current Dealer Hand Value: {dealer.value}")



playing = True
chips = Chips(200)

while True:
    win = False
    playerBusted = False
    print("Welcome to Python BlackJack")

    cardDeck = Deck()
    player = Hand()
    dealer = Hand()
    cardDeck.shuffle()
    initGame(cardDeck, player, dealer)
    chips.bet = placeBet(chips)
    showSome(player, dealer)

    while playing:
        hitOrStand(player, cardDeck)
        showSome(player, dealer)

        if(player.value > 21): 
            playerBusts(chips)
            break

    if(player.value <= 21):
        showAll(player, dealer)
        while(dealer.value < 17):
            hit(dealer, cardDeck)

        showAll(player, dealer)
        if(dealer.value > 21):
            dealerBust(chips)

        elif(dealer.value > player.value):
            dealerWins(chips)
        
        elif(dealer.value < player.value):
            playerWins(chips)
        else:
            push()

    print(f"\nTotal chips remaining: {chips.total}")
    choice = input("would you like to play again? enter y for yes, anything else to quit \n").lower()
    if (choice != 'y'):
        break

