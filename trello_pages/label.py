from config import trello
from logs.logging_setup import logger


class LabelElements:
    def __init__(self):
        self.create_label_response = 0
        self.get_label_response = 0
        self.update_label_response = 0

    def create_label(self, base_url, url_for_label, querystring):
        url = base_url + url_for_label
        response = trello.post(url, params=querystring)
        if response.status_code >= 400:
            logger.debug('There was an error in creating label')
            return response
        else:
            logger.debug('Label successfully created')
            self.create_label_response = response

    def get_label(self, base_url, url_for_label, label_id, querystring):
        url = base_url + url_for_label + label_id
        response = trello.get(url, params=querystring)
        if response.status_code >= 400:
            logger.debug('There was an error in creating label')
            return response
        else:
            logger.debug('Label successfully created')
            self.get_label_response = response

    def update_label(self, base_url, url_for_label, label_id, querystring, url_to_update_label_name):
        url = base_url + url_for_label + label_id + url_to_update_label_name
        response = trello.put(url, params=querystring)
        if response.status_code >= 400:
            logger.debug('There was an error in creating label')
            return response
        else:
            logger.debug('Label successfully created')
            self.update_label_response = response


label = LabelElements()
