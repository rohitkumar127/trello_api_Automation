from trello_pages.list import trello_list
from trello_pages.boards import board
from utility.constants import *
from logs.logging_setup import *
import pytest


class TestLists:
    @staticmethod
    def compare_values(actual_value, expected_value):
        try:
            assert actual_value == expected_value
            logger.debug("Test Successful")
        except AssertionError:
            logger.exception('Assertion error')
            pytest.fail('Assertion error', pytrace=True)

    @pytest.mark.post
    @pytest.mark.usefixtures("list_setup")
    def test_list_successful_creation_tc8(self):
        self.compare_values(trello_list.create_list_response.status_code, 200)

    @pytest.mark.post
    @pytest.mark.usefixtures("list_setup")
    def test_list_successful_creation_by_list_name_tc9(self):
        self.compare_values(trello_list.create_list_response.json()['name'], first_list_name)

    @pytest.mark.negative_test
    @pytest.mark.usefixtures("board_setup")
    def test_list_unsuccessful_creation_tc10(self):
        """creating invalid list by providing it with boardId in integer form rather than string form"""
        querystring_for_list['idBoard'] = 12344
        trello_list.create_list(base_url=base_url, url_for_list=url_for_list,
                                querystring=querystring_for_list)
        self.compare_values(trello_list.create_list_response.status_code, 400)

    @pytest.mark.negative_test
    @pytest.mark.usefixtures("board_setup")
    def test_list_unsuccessful_creation_providing_invalid_board_id_tc11(self):
        """creating invalid list by providing it with boardId which is invalid"""
        querystring_for_list['idBoard'] = "12344"
        trello_list.create_list(base_url=base_url, url_for_list=url_for_list,
                                querystring=querystring_for_list)
        self.compare_values(trello_list.create_list_response.status_code, 400)

    @pytest.mark.update
    @pytest.mark.usefixtures("list_setup")
    def test_update_list_name_tc12(self):
        querystring_for_list["name"] = updated_list_name
        querystring_for_list["idBoard"] = board.create_board_response.json()['id']
        trello_list.update_list_details(base_url=base_url, url_for_list=url_for_list,
                                        list_id=trello_list.create_list_response.json()['id'],
                                        querystring=querystring_for_list)
        self.compare_values(trello_list.update_list_response.json()['name'], updated_list_name)

    @pytest.mark.get
    @pytest.mark.usefixtures("list_setup")
    def test_getting_list_data_tc13(self):
        trello_list.get_list_details(base_url=base_url, url_for_list=url_for_list,
                                     list_id=trello_list.create_list_response.json()['id'])
        self.compare_values(trello_list.get_list_response.json()['name'], first_list_name)
