import random
import Player_Cards as pc


class Deck:
    def __init__(self, list):
        standard_deck = [pc.strike, pc.strike, pc.strike, pc.strike, pc.strike,
                         pc.strike, pc.block, pc.block, pc.block, pc.block, pc.block, pc.block]
        self.list = []
        self.player_deck = standard_deck

    def shuffle(self):
        random.shuffle(self.list)


deck.shuffle()


draw_pile.shuffle() = Deck([])
discard_pile = Deck([])
hand = Deck([])
exhaust = Deck([])
player_deck = Deck([])

draw_pile.list = player_deck.list


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


shuffle_deck(draw_pile)

print(draw_pile.list)
print(discard_pile.list)
print(player_deck.list)
print(hand.list)
print(exhaust.list)
