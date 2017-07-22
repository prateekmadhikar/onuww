from onuwwo.models.socket_holder import SocketHolder


class Roles:

    DOPPELGANGER = 0
    DRUNK = 1
    HUNTER = 2
    INSOMNIAC = 3
    MASON = 4
    MINION = 5
    ROBBER = 6
    SEER = 7
    TANNER = 8
    TROUBLEMAKER = 9
    VILLAGER = 10
    WEREWOLF = 11


class Player(SocketHolder):

    def __init__(self, id, socket, role, is_creator=False):
        super(Player, self).__init__(id, socket)

        self._current_role = role
        self._original_role = role
        self._id = id
        self._is_creator = is_creator

    def __eq__(self, other):
        return self.id == other.id
