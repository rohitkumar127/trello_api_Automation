from trello_pages.cards import cards
from trello_pages.list import trello_list
from utility.constants import *
import pytest
from logs.logging_setup import logger


class TestCards:
    @staticmethod
    def compare_values(actual_value, expected_value):
        try:
            assert actual_value == expected_value
            logger.debug("Test Successful")
        except AssertionError:
            logger.exception('Assertion error')
            pytest.fail('Assertion error', pytrace=True)

    @pytest.mark.post
    @pytest.mark.usefixtures("card_setup")
    def test_card_successful_creation_tc14(self):
        self.compare_values(cards.create_card_response.status_code, 200)

    @pytest.mark.post
    @pytest.mark.usefixtures("card_setup")
    def test_card_successful_creation_by_name_tc15(self):
        self.compare_values(cards.create_card_response.json()['name'], first_card_name)

    @pytest.mark.negative_test
    @pytest.mark.usefixtures("list_setup")
    def test_card_unsuccessful_creation_tc16(self):
        """creating a card with invalid listId so that it gives 400 or bad request error"""
        querystring_for_cards['name'] = first_card_name
        querystring_for_cards['idList'] = "1234567"
        cards.create_card(base_url=base_url, url_for_cards=url_for_cards, querystring=querystring_for_cards)
        self.compare_values(cards.create_card_response.status_code, 400)

    @pytest.mark.negative_test
    @pytest.mark.usefixtures("list_setup")
    def test_card_unsuccessful_creation_using_invalid_url(self):
        """creating a card with invalid url should give 404 or page not found error"""
        querystring_for_cards['name'] = first_card_name
        querystring_for_cards['idList'] = trello_list.create_list_response.json()['id']
        cards.create_card(base_url=base_url, url_for_cards=invalid_card_url,
                          querystring=querystring_for_cards)
        self.compare_values(cards.create_card_response.status_code, 404)

    @pytest.mark.get
    @pytest.mark.usefixtures("card_setup")
    def test_getting_card_data(self):
        cardId = cards.create_card_response.json()['id']
        cards.get_card_details(base_url=base_url, url_for_cards=url_for_cards, card_id=cardId)
        self.compare_values(cards.get_card_response.status_code, 200)

    @pytest.mark.get
    @pytest.mark.usefixtures("card_setup")
    def test_getting_card_data_verifying_name(self):
        cardId = cards.create_card_response.json()['id']
        cards.get_card_details(base_url=base_url, url_for_cards=url_for_cards, card_id=cardId)
        self.compare_values(cards.get_card_response.json()['name'], first_card_name)

    @pytest.mark.update
    @pytest.mark.usefixtures("card_setup")
    def test_update_card_data(self):
        cardId = cards.create_card_response.json()['id']
        querystring_for_cards['name'] = updated_card_name
        querystring_for_cards['idList'] = trello_list.create_list_response.json()['id']
        cards.update_card_details(base_url=base_url, url_for_cards=url_for_cards, querystring=querystring_for_cards,
                                  card_id=cardId)
        self.compare_values(cards.update_card_response.json()['name'], updated_card_name)

    @pytest.mark.delete
    @pytest.mark.usefixtures("card_setup")
    def test_deleting_card_successfully(self):
        cardId = cards.create_card_response.json()['id']
        cards.delete_card(base_url=base_url, url_for_cards=url_for_cards, card_id=cardId)
        self.compare_values(cards.delete_card_response.status_code, 200)

    @pytest.mark.negative_test
    @pytest.mark.usefixtures("card_setup")
    def test_deleting_card_which_is_nor_present(self):
        """providing a card with invalid card id while deleting it, it will result in bad request since it will not
        find card with that id"""
        response = cards.delete_card(base_url=base_url, url_for_cards=url_for_cards, card_id=invalid_card_id)
        self.compare_values(cards.delete_card_response.status_code, 400)
