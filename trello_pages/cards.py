from utility.config import trello
from logs.logging_setup import logger


class CardsElements:
    def __init__(self):
        pass

    def create_card(self, base_url, url_for_cards, querystring):
        url = base_url + url_for_cards
        response = trello.post(url, params=querystring)
        if response.status_code == 200:
            logger.debug('Card successfully created')
        else:
            logger.debug('Error in creating card')
        self.create_card_response = response

    def get_card_details(self, base_url, url_for_cards, card_id):
        url = base_url + url_for_cards + card_id
        response = trello.get(url)
        if response.status_code == 200:
            logger.debug('Card data successfully received')
        else:
            logger.debug('Error in getting card data')
        self.get_card_response = response

    def update_card_details(self, base_url, url_for_cards, card_id, querystring):
        url = base_url + url_for_cards + card_id
        response = trello.put(url, params=querystring)
        if response.status_code == 200:
            logger.debug('Card successfully updated')
        else:
            logger.debug('Error in updating card')
        self.update_card_response = response

    def delete_card(self, base_url, url_for_cards, card_id):
        url = base_url + url_for_cards + card_id
        response = trello.delete(url)
        if response.status_code == 200:
            logger.debug('Card successfully deleted')
        else:
            logger.debug('Error in deleting card')
        self.delete_card_response = response


cards = CardsElements()
