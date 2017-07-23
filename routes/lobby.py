import httplib

from flask import Blueprint
from flask import request

from services.game_room import GameRoomService
from utils.http_utils import JSONResponse

lobby_blueprint = Blueprint('lobby', __name__)
game_room_service = GameRoomService()


@lobby_blueprint.route('/game_rooms', methods=['GET'])
def list_games():
    game_rooms = game_room_service.get_rooms()

    data = {
        'data': [game_rooms[id].to_dict() for id in game_rooms.iterkeys()]
    }

    return JSONResponse(data)


@lobby_blueprint.route('/game_rooms', methods=['POST'])
def create_game():
    game_data = request.json

    try:
        name = game_data['name']
        password = game_data.get('password', None)
    except KeyError:
        return JSONResponse({'message': 'Expect name for game'}, status_code=httplib.BAD_REQUEST)

    game_room = game_room_service.create_room(name, password=password)

    return JSONResponse({'message': 'Created game with name {}'.format(game_room.id)}, status_code=httplib.OK)
