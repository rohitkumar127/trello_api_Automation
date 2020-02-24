from config import trello
from logs.logging_setup import *


class MemberElements:
    def __init__(self):
        self.create_board_member_response = 0
        self.get_board_member_response = 0

    def create_board_member(self, base_url, url_for_board, board_id, url_for_member, querystring):
        url = base_url + url_for_board + board_id + url_for_member
        response = trello.put(url, params=querystring)
        if response.status_code >= 400:
            logger.debug('There was an error in updating board data')
            return response
        else:
            logger.debug('Board data updated received')
            self.create_board_member_response = response

    def get_board_member(self, base_url, url_for_board, board_id, url_for_member):
        url = base_url + url_for_board + board_id + url_for_member
        response = trello.get(url)
        if response.status_code >= 400:
            logger.debug('There was an error in updating board data')
            return response
        else:
            logger.debug('Board data updated received')
            self.get_board_member_response = response

    def get_member(self, base_url, url_for_member, member_id):
        """getting member by specifying member id"""
        url = base_url + url_for_member + member_id
        response = trello.get(url)
        if response.status_code >= 400:
            logger.debug('There was an error in updating board data')
            return response
        else:
            logger.debug('Board data updated received')
            self.get_board_member_response = response


member = MemberElements()
