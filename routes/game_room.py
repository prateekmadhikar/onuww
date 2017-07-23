from flask import Blueprint

from services.game_room import GameRoomService

game_room_blueprint = Blueprint('lobby', __name__)
game_room_service = GameRoomService()


@game_room_blueprint.route('/game_rooms/{game_room_id}')
def join_game(game_rood_id):
    pass
