import Deck_managing as dm


class Player:
    def __init__(self, hp, max_mana):
        self.hp = hp
        self.max_mana = max_mana
        self.mana = self.max_mana
        self.block = 0

    def refresh_mana(self):
        self.mana = self.max_mana

    def reset_block(self):
        self.block = 0

    def end_of_turn(self):
        self.refresh_mana()
        self.reset_block()


class Monster:
    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage


def player_action(player, monster):
    while player.mana > 0:
        card_choice = int(input(
            "Use a skill\nPress 1 for Strike\nPress 2 for Block\nPress 3 to end your turn\n: "))

        if card_choice == 1:
            monster.hp -= dm.strike.damage
            player.mana -= dm.strike.cost
            print("You inflict one damage")
            if monster.hp <= 0:
                break
        elif card_choice == 2:
            player.block += dm.block.block
            player.mana -= dm.block.cost
            print("You block 1 damage")
        elif card_choice == 3:
            break
        else:
            print("Faulty input!")


def monster_action(player, monster):
    damage_this_turn = monster.damage - player.block
    if damage_this_turn > 0:
        player.hp -= damage_this_turn


def win_condition(monster):
    if monster.hp > 0:
        return False
    return True


def lose_condition(player):
    if player.hp > 0:
        return False
    return True


def encounter(player, monster):
    while player.hp > 0 and monster.hp > 0:
        # refresh_cards

        player_action(player, monster)
        if win_condition(monster) == True:
            print("You won!")
            break

        monster_action(player, monster)
        if lose_condition(player) == True:
            print("You lost!")
            break
        player.end_of_turn()
        print(" ")
        print("Player_ HP =", player.hp)
        print("Player mana =", player.mana)
        print("Monster HP =", monster.hp)
        print(" ")
        # break


player = Player(4, 3)
monster = Monster(4, 2)


encounter(player, monster)
