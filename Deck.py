from Card import Card
import random

class Deck:
    def __init__(self):
        self.deck = []
        suits = ('Hearts', 'Diamonds', 'Clovers', 'Spades')
        ranks = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

        for suit in suits:
            for rank, value in ranks.items():
                self.deck.append(Card(suit = suit, rank = rank, value = value))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

    def __str__(self) :
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n'+ card.__str__()
        return f"The deck has: {deck_comp}"
