import random
import Slay_the_spire as sts
class Deck:
    def __init__(self, list):
        self.list = []
        standard_deck = [sts.strike, sts.strike, sts.strike, sts.strike, sts.strike,
                         sts.strike, sts.block, sts.block, sts.block, sts.block, sts.block, sts.block]
        self.player_deck = standard_deck


draw_pile = Deck([])
discard_pile = Deck([])
hand = Deck([])
exhaust = Deck([])
player_deck = Deck([])

player_deck.list = (1, 2, 3, 4, 5, 6, 7, 8, 9)
draw_pile.list = player_deck.list

# draw_pile.list.append(1)
# draw_pile.list.append(1)
# draw_pile.list.append(2)
# draw_pile.list.append(2)

def shuffle_deck(deck):
    random.shuffle(deck)

def move_card(from_deck, to_deck, index):
    to_deck.append(from_deck[index])
    from_deck.remove(from_deck[index])

def empty_discard_pile():
    shuffle_deck(discard_pile)
    while len(discard_pile) > 0:
        move_card(discard_pile, draw_pile, 0)

def draw_cards(number_of_cards):  # Detta håller vi på med :)
    for index in number_of_cards:
        if len(draw_pile) == 0:
            empty_discard_pile()

        move_card(draw_pile, hand, 0)

# print(draw_pile.list)
# shuffle_deck(draw_pile.list)
# print(draw_pile.list)


shuffle_deck(draw_pile)

print(draw_pile.list)
print(discard_pile.list)
print(player_deck.list)
print(hand.list)
print(exhaust.list)

# print("draw_pile" + draw_pile.list)
# print("discard_pile" + discard_pile.list)
# print("player_deck" + player_deck.list)
