from config import trello
from logs.logging_setup import logger


class ListElements:
    def __init__(self):
        self.create_list_response = 0
        self.update_list_response = 0
        self.get_list_response = 0

    def create_list(self, base_url, url_for_list, querystring):
        url = base_url + url_for_list
        response = trello.post(url, params=querystring)
        if response.status_code >= 400:
            logger.debug('There was an error in creating list')
            return response
        else:
            logger.debug('List successfully created')
            self.create_list_response = response

    def get_list_details(self, base_url, url_for_list, list_id):
        url = base_url + url_for_list + list_id
        response = trello.get(url)
        if response.status_code >= 400:
            logger.debug('There was an error in getting list data')
            return response
        else:
            logger.debug('List data successfully received')
            self.get_list_response = response

    def update_list_details(self, base_url, url_for_list, list_id, querystring):
        url = base_url + url_for_list + list_id
        response = trello.put(url, params=querystring)
        if response.status_code >= 400:
            logger.debug('There was an error in updating card')
            return response
        else:
            logger.debug('Card data successfully updated')
            self.update_list_response = response


trello_list = ListElements()
