from utility.config import trello
from logs.logging_setup import *


class MemberElements:
    def __init__(self):
        pass

    def create_board_member(self, base_url, url_for_board, board_id, url_for_member, querystring):
        url = base_url + url_for_board + board_id + url_for_member
        response = trello.put(url, params=querystring)
        if response.status_code == 200:
            logger.debug('Board member successfully created')
        else:
            logger.debug('Board member creation failed')
        self.create_board_member_response = response

    def get_board_member(self, base_url, url_for_board, board_id, url_for_member):
        url = base_url + url_for_board + board_id + url_for_member
        response = trello.get(url)
        if response.status_code == 200:
            logger.debug('Board member data successfully received')
        else:
            logger.debug('Board member data not received')
        self.get_board_member_response = response

    def get_member(self, base_url, url_for_member, member_id):
        """getting member by specifying member id"""
        url = base_url + url_for_member + member_id
        response = trello.get(url)
        if response.status_code == 200:
            logger.debug('Board member data successfully received')
        else:
            logger.debug('Board member data not received')
        self.get_board_member_response = response

    def get_member_notifications(self, base_url, url_for_member, member_id, url_for_notifications):
        """getting member by specifying member id"""
        url = base_url + url_for_member + member_id + url_for_notifications
        response = trello.get(url)
        if response.status_code == 200:
            logger.debug('Board member notification received')
        else:
            logger.debug('Board member notification not received')
        self.get_member_notifications_response = response

    # def creating_avatar_for_member(self, base_url, url_for_member, member_id, url_for_avatar, querystring):
    #     url = base_url + url_for_member + member_id + url_for_avatar
    #     response = trello.post(url, params=querystring)
    #     if response.status_code >= 400:
    #         logger.debug('There was an error in updating board data')
    #         return response
    #     else:
    #         logger.debug('Board data updated received')
    #         self.member_avatar_response = response


member = MemberElements()
