from Card import Card
from Deck import Deck

deck = Deck()

poppedcard = deck.deal()
deck.shuffle()
for card in deck.deck:
    print(card)
print(f"deck amount: {len(deck.deck)}")
print(f"i have been popped {poppedcard}")