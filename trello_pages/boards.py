from utility.config import trello
from logs.logging_setup import *


class BoardElements:
    def __init__(self):
        pass

    def create_board(self, base_url, url_for_board, querystring):
        url = base_url + url_for_board
        response = trello.post(url, params=querystring)
        if response.status_code == 200:
            logger.debug("Board successfully created")
        else:
            logger.debug("Error in creating board")
        self.create_board_response = response

    def get_board_details(self, base_url, url_for_board, board_id):
        url = base_url + url_for_board + board_id
        response = trello.get(url)
        if response.status_code == 200:
            logger.debug("Board data successfully received")
        else:
            logger.debug("Error in getting board data")
        self.get_board_response = response

    def update_board_details(self, base_url, url_for_board, board_id, querystring):
        url = base_url + url_for_board + board_id
        response = trello.put(url, params=querystring)
        if response.status_code == 200:
            logger.debug("Board successfully updated")
        else:
            logger.debug("Error in updating board")
        self.update_board_response = response

    def delete_board(self, base_url, url_for_board, board_id):
        url = base_url + url_for_board + board_id
        response = trello.delete(url)
        if response.status_code == 200:
            logger.debug("Board successfully deleted")
        else:
            logger.debug("Error in deleting board")
        self.delete_board_response = response


board = BoardElements()
