from trello_elements.boards import board
from constants import *


class TestBoards:
    def test_board_successful_creation(self, board_setup):
        assert board.create_board_response.status_code == 200
        assert board.create_board_response.json()['name'] == first_board_name

    def test_create_invalid_board(self):
        """create invalid board  situation by providing wrong board url"""
        response = board.create_board(base_url=base_url, url_for_board=invalid_board_url,
                                      querystring=querystring_for_board)
        assert response.status_code == 404

    def test_successful_board_update(self, board_setup):
        boardId = board.create_board_response.json()['id']
        querystring_for_board['name'] = board_updated_name
        board.update_board_details(base_url=base_url, url_for_board=url_for_board, board_id=boardId,
                                   querystring=querystring_for_board)
        assert board.update_board_response.status_code == 200
        assert board.update_board_response.json()['name'] == board_updated_name

    def test_successful_board_get_request(self, board_setup):
        boardId = board.create_board_response.json()['id']
        board.get_board_details(base_url=base_url, url_for_board=url_for_board, board_id=boardId)
        assert board.get_board_response.status_code == 200
        assert board.get_board_response.json()['name'] == first_board_name

    def test_board_deletion(self, board_setup):
        boardId = board.create_board_response.json()['id']
        board.delete_board(base_url=base_url, url_for_board=url_for_board, board_id=boardId)
        assert board.delete_board_response.status_code == 200
