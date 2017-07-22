class GameRoom:

    def __init__(self, id):
        self.id = id
        self.players = []

    @property
    def num_players(self):
        return len(self.players)

    def add_player(self, player):
        if not self.has_player(player):
            self.players.append(player)
            return True
        return False

    def remove_player(self, player):
        if self.has_player(player):
            self.players.remove(player)
            return True
        return False
