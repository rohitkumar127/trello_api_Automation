from trello_elements.list import trello_list
from trello_elements.boards import board
from constants import *


class TestLists:
    def test_list_successful_creation(self, list_setup):
        assert trello_list.create_list_response.status_code == 200
        assert trello_list.create_list_response.json()['name'] == first_list_name

    def test_list_unsuccessful_creation(self, list_setup):
        """creating invalid list by providing it with boardId in integer form rather than string form"""
        querystring_for_list['idBoard'] = 12344
        response = trello_list.create_list(base_url=base_url, url_for_list=url_for_list,
                                           querystring=querystring_for_list)
        assert response.status_code == 400

    def test_list_unsuccessful_creation_providing_invalid_board_id(self, list_setup):
        """creating invalid list by providing it with boardId in integer form rather than string form"""
        querystring_for_list['idBoard'] = "12344"
        response = trello_list.create_list(base_url=base_url, url_for_list=url_for_list,
                                           querystring=querystring_for_list)
        assert response.status_code == 400

    def test_update_list_name(self, list_setup):
        querystring_for_list["name"] = updated_list_name
        querystring_for_list["idBoard"] = board.create_board_response.json()['id']
        trello_list.update_list_details(base_url=base_url, url_for_list=url_for_list,
                                        list_id=trello_list.create_list_response.json()['id'],
                                        querystring=querystring_for_list)
        assert trello_list.update_list_response.status_code == 200
        assert trello_list.update_list_response.json()['name'] == updated_list_name


