class Room:

    def __init__(self, id, controller):
        self.id = id
        self.players = []
        self.game_controller = controller

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
