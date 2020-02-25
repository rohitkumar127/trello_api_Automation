from trello_pages.boards import board
from utility.constants import *
from logs.logging_setup import *
import pytest



class TestBoards:
    @staticmethod
    def compare_values(actual_value, expected_value):
        try:
            assert actual_value == expected_value
            logger.debug("Test Successful")
        except AssertionError:
            logger.exception('Assertion error')
            pytest.fail('Assertion error', pytrace=True)

    @pytest.mark.post
    @pytest.mark.usefixtures("board_setup")
    def test_board_successful_creation_tc1(self):
        self.compare_values(board.create_board_response.status_code, 200)

    @pytest.mark.negative_test
    def test_create_invalid_board_tc2(self):
        """create invalid board  situation by providing wrong board url which will give 404 or page not found error"""
        board.create_board(base_url=base_url, url_for_board=invalid_board_url,
                           querystring=querystring_for_board)
        self.compare_values(board.create_board_response.status_code, 404)

    @pytest.mark.update
    @pytest.mark.usefixtures("board_setup")
    def test_successful_board_update_tc3(self, base_url):
        boardId = board.create_board_response.json()['id']
        querystring_for_board['name'] = board_updated_name
        board.update_board_details(base_url=base_url, url_for_board=url_for_board, board_id=boardId,
                                   querystring=querystring_for_board)
        self.compare_values(board.update_board_response.status_code, 200)

    @pytest.mark.update
    @pytest.mark.usefixtures("board_setup")
    def test_successful_board_update_by_name_tc4(self, base_url):
        boardId = board.create_board_response.json()['id']
        querystring_for_board['name'] = board_updated_name
        board.update_board_details(base_url=base_url, url_for_board=url_for_board, board_id=boardId,
                                   querystring=querystring_for_board)
        self.compare_values(board.update_board_response.json()['name'], board_updated_name)

    @pytest.mark.get
    @pytest.mark.usefixtures("board_setup")
    def test_successful_board_get_request_tc5(self, base_url):
        boardId = board.create_board_response.json()['id']
        board.get_board_details(base_url=base_url, url_for_board=url_for_board, board_id=boardId)
        self.compare_values(board.get_board_response.status_code, 200)

    @pytest.mark.get
    @pytest.mark.usefixtures("board_setup")
    def test_successful_board_get_request_by_name_tc6(self, base_url):
        boardId = board.create_board_response.json()['id']
        board.get_board_details(base_url=base_url, url_for_board=url_for_board, board_id=boardId)
        self.compare_values(board.get_board_response.json()['name'], first_board_name)

    @pytest.mark.delete
    @pytest.mark.usefixtures("board_setup")
    def test_board_deletion_tc7(self, base_url):
        boardId = board.create_board_response.json()['id']
        board.delete_board(base_url=base_url, url_for_board=url_for_board, board_id=boardId)
        self.compare_values(board.delete_board_response.status_code, 200)
