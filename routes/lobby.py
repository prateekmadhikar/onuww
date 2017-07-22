from flask import Blueprint
from flask import jsonify

from services.game_room import GameRoomService
from utils.http_utils import JSONResponse

lobby_blueprint = Blueprint('lobby', __name__)
game_room_service = GameRoomService()


@lobby_blueprint.route('/game_rooms', methods=['GET'])
def list_games():
    game_rooms = game_room_service.get_rooms()

    data = {
        'data': game_rooms
    }

    return JSONResponse(data)


@lobby_blueprint.route('/game_rooms', methods=['POST'])
def create_game():
    return 'derp', 200
