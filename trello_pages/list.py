from config import trello
from logs.logging_setup import logger


class ListElements:
    def __init__(self):
        pass

    def create_list(self, base_url, url_for_list, querystring):
        url = base_url + url_for_list
        response = trello.post(url, params=querystring)
        if response.status_code == 200:
            logger.debug('List successfully created')
        else:
            logger.debug('Error in creating list')
        self.create_list_response = response

    def get_list_details(self, base_url, url_for_list, list_id):
        url = base_url + url_for_list + list_id
        response = trello.get(url)
        if response.status_code == 200:
            logger.debug('List data successfully received')
        else:
            logger.debug('Error in getting list')
        self.get_list_response = response

    def update_list_details(self, base_url, url_for_list, list_id, querystring):
        url = base_url + url_for_list + list_id
        response = trello.put(url, params=querystring)
        if response.status_code == 200:
            logger.debug('List successfully updated')
        else:
            logger.debug('Error in updating list')
        self.update_list_response = response


trello_list = ListElements()
