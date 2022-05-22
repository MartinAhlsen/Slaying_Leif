class Player_Cards:
    def __init__(self, name, cost, damage, block):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.block = block
    
strike = Player_Cards("Strike", 1, 1, 0)
block = Player_Cards("Block", 1, 0, 1)