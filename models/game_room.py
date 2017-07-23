class GameRoom:

    def __init__(self, id, password=None):
        self.id = id
        self._players = []
        self._password = password

    @property
    def num_players(self):
        return len(self._players)

    def add_player(self, player):
        if not self.has_player(player):
            self._players.append(player)
            return True
        return False

    def remove_player(self, player):
        if self.has_player(player):
            self._players.remove(player)
            return True
        return False

    def to_dict(self):
        dict = {
            'id': self.id,
            'num_players': self.num_players,
            'password_protected': True
        }

        return dict
