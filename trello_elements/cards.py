from config import trello


class CardsElements:
    def __init__(self):
        pass

    def create_card(self, base_url, url_for_cards, querystring):
        url = base_url + url_for_cards
        response = trello.post(url, params=querystring)
        return response

    def get_card_details(self, base_url, url_for_cards, card_id):
        url = base_url + url_for_cards + card_id
        response = trello.get(url)
        return response

    def update_card_details(self, base_url, url_for_cards, card_id, querystring):
        url = base_url + url_for_cards + card_id
        response = trello.put(url, params=querystring)
        return response

    def delete_card(self, base_url, url_for_cards, card_id):
        url = base_url + url_for_cards + card_id
        response = trello.delete(url)
        return response


cards = CardsElements()
