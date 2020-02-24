from trello_pages.boards import board
from trello_pages.label import label
from constants import *


class TestLabel:
    def test_create_label(self, board_setup):
        querystring_for_label['idBoard'] = board.create_board_response.json()['id']
        label.create_label(base_url=base_url, url_for_label=url_for_label, querystring=querystring_for_label)
        assert label.create_label_response.status_code == 200

    def test_get_label_response(self, board_setup):
        querystring_for_label['idBoard'] = board.create_board_response.json()['id']
        label.create_label(base_url=base_url, url_for_label=url_for_label, querystring=querystring_for_label)
        label.get_label(base_url=base_url, url_for_label=url_for_label,
                        label_id=label.create_label_response.json()['id'], querystring=querystring_for_get_label)
        assert label.get_label_response.status_code == 200

    def test_get_label_name(self, board_setup):
        querystring_for_label['idBoard'] = board.create_board_response.json()['id']
        label.create_label(base_url=base_url, url_for_label=url_for_label, querystring=querystring_for_label)
        label.get_label(base_url=base_url, url_for_label=url_for_label,
                        label_id=label.create_label_response.json()['id'], querystring=querystring_for_get_label)
        assert label.get_label_response.json()['name'] == querystring_for_label['name']

    def test_update_label_name(self, board_setup):
        querystring_for_label['idBoard'] = board.create_board_response.json()['id']
        label.create_label(base_url=base_url, url_for_label=url_for_label, querystring=querystring_for_label)
        response = label.update_label(base_url=base_url, url_for_label=url_for_label,
                                      label_id=label.create_label_response.json()['id'],
                                      querystring=querystring_for_updated_label_name,
                                      url_to_update_label_name=url_to_update_label_name)
        assert label.update_label_response.json()['name'] == querystring_for_updated_label_name['value']
