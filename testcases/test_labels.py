from trello_pages.boards import board
from trello_pages.label import label
from constants import *
import pytest
from logs.logging_setup import logger


class TestLabel:
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
    def test_create_label(self):
        querystring_for_label['idBoard'] = board.create_board_response.json()['id']
        label.create_label(base_url=base_url, url_for_label=url_for_label, querystring=querystring_for_label)
        self.compare_values(label.create_label_response.status_code, 200)

    @pytest.mark.get
    @pytest.mark.usefixtures("board_setup")
    def test_get_label_response(self):
        querystring_for_label['idBoard'] = board.create_board_response.json()['id']
        label.create_label(base_url=base_url, url_for_label=url_for_label, querystring=querystring_for_label)
        label.get_label(base_url=base_url, url_for_label=url_for_label,
                        label_id=label.create_label_response.json()['id'], querystring=querystring_for_get_label)
        self.compare_values(label.get_label_response.status_code, 200)

    @pytest.mark.get
    @pytest.mark.usefixtures("board_setup")
    def test_get_label_name(self):
        querystring_for_label['idBoard'] = board.create_board_response.json()['id']
        label.create_label(base_url=base_url, url_for_label=url_for_label, querystring=querystring_for_label)
        label.get_label(base_url=base_url, url_for_label=url_for_label,
                        label_id=label.create_label_response.json()['id'], querystring=querystring_for_get_label)
        self.compare_values(label.get_label_response.json()['name'], querystring_for_label['name'])

    @pytest.mark.update
    @pytest.mark.usefixtures("board_setup")
    def test_update_label_name(self):
        querystring_for_label['idBoard'] = board.create_board_response.json()['id']
        label.create_label(base_url=base_url, url_for_label=url_for_label, querystring=querystring_for_label)
        label.update_label(base_url=base_url, url_for_label=url_for_label,
                           label_id=label.create_label_response.json()['id'],
                           querystring=querystring_for_updated_label_name,
                           url_to_update_label_name=url_to_update_label_name)
        self.compare_values(label.update_label_response.json()['name'], querystring_for_updated_label_name['value'])
