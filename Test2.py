import random
import Slaying_Leif as sts
class Deck:
    def __init__(self, list):
        self.list = []
#        standard_deck = [sts.strike, sts.strike, sts.strike, sts.strike, sts.strike,
#                         sts.strike, sts.block, sts.block, sts.block, sts.block, sts.block, sts.block]
#        self.player_deck = standard_deck


draw_pile = Deck([])
discard_pile = Deck([])
hand = Deck([])
exhaust = Deck([])
player_deck = Deck([])

def shuffle_deck(deck):
    random.shuffle(deck)

def move_card(from_deck, to_deck, index):
    to_deck.append(from_deck[index])
    from_deck.remove(from_deck[index])

def empty_discard_pile():
    shuffle_deck(discard_pile.list)
    while len(discard_pile.list) > 0:
        move_card(discard_pile.list, draw_pile.list, 0)

def draw_cards(number_of_cards):  # Detta håller vi på med :)
    for not_used in range(number_of_cards):
        if len(draw_pile.list) == 0:
            empty_discard_pile()
        move_card(draw_pile.list, hand.list, 0)

draw_pile.list = [sts.strike, sts.strike, sts.strike, sts.strike, sts.strike,
                         sts.strike, sts.block, sts.block, sts.block, sts.block, sts.block, sts.block]
discard_pile.list = []


print(draw_pile.list)
print(discard_pile.list)
print(hand.list)

draw_cards(5)

print(draw_pile.list)
print(discard_pile.list)
print(hand.list)