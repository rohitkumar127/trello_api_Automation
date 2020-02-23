import pytest
from trello_elements.boards import board
from trello_elements.list import trello_list
from constants import *


@pytest.yield_fixture()
def board_setup():
    querystring_for_board['name'] = first_board_name
    board.create_board(base_url=base_url, url_for_board=url_for_board,
                       querystring=querystring_for_board)
    yield
    board.delete_board(base_url=base_url, url_for_board=url_for_board,
                       board_id=board.create_board_response.json()['id'])


@pytest.yield_fixture()
def list_setup():
    querystring_for_board['name'] = first_board_name
    board.create_board(base_url=base_url, url_for_board=url_for_board,
                       querystring=querystring_for_board)
    querystring_for_list["name"] = first_list_name
    querystring_for_list["idBoard"] = board.create_board_response.json()['id']
    trello_list.create_list(base_url=base_url, url_for_list=url_for_list, querystring=querystring_for_list)
    yield
    board.delete_board(base_url=base_url, url_for_board=url_for_board,
                       board_id=board.create_board_response.json()['id'])