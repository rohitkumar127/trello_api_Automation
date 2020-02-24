from config import trello
from logs.logging_setup import logger


class CardsElements:
    def __init__(self):
        self.create_card_response = 0
        self.get_card_response = 0
        self.update_card_response = 0
        self.delete_card_response = 0

    def create_card(self, base_url, url_for_cards, querystring):
        url = base_url + url_for_cards
        response = trello.post(url, params=querystring)
        if response.status_code >= 400:
            logger.debug('There was an error in creating card')
            return response
        else:
            logger.debug('Card successfully created')
            self.create_card_response = response

    def get_card_details(self, base_url, url_for_cards, card_id):
        url = base_url + url_for_cards + card_id
        response = trello.get(url)
        if response.status_code >= 400:
            logger.debug('There was an error in getting card data')
            return response
        else:
            logger.debug('Card data successfully received')
            self.get_card_response = response

    def update_card_details(self, base_url, url_for_cards, card_id, querystring):
        url = base_url + url_for_cards + card_id
        response = trello.put(url, params=querystring)
        if response.status_code >= 400:
            logger.debug('There was an error in updating card details')
            return response
        else:
            logger.debug('Card data successfully updated')
            self.update_card_response = response

    def delete_card(self, base_url, url_for_cards, card_id):
        url = base_url + url_for_cards + card_id
        response = trello.delete(url)
        if response.status_code >= 400:
            logger.debug('There was an error in deleting card')
            return response
        else:
            logger.debug('Card successfully deleted')
            self.delete_card_response = response


cards = CardsElements()
