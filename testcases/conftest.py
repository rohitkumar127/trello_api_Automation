import pytest
from trello_elements.boards import board
from constants import *


@pytest.yield_fixture()
def board_setup():
    querystring_for_board['name'] = first_board_name
    response = board.create_board(base_url=base_url, url_for_board=url_for_board,
                                  querystring=querystring_for_board)
    yield response
    board.delete_board(base_url=base_url, url_for_board=url_for_board,
                       board_id=board.create_board_response.json()['id'])
