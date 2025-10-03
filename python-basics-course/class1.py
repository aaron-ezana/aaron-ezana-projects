class Player:
    def __init__(self, name, position, number):
        self.name = name
        self.position = position
        self.number = number
    
    def academy_player(self):
        return self.number > 25