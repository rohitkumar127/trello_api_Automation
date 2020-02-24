from trello_pages.boards import board
from trello_pages.member import member
from constants import *


class TestMember:
    def test_board_member_successful_creation(self, member_setup):
        assert member.create_board_member_response.status_code == 200
        assert member.create_board_member_response.json()['members'][1]['fullName'] == querystring_for_member[
            'fullName']

    def test_board_member_unsuccessful_creation(self):
        """creating a member without an email address will give an error saying invalid email address"""
        board_id = board.create_board_response.json()['id']
        response = member.create_board_member(base_url=base_url, url_for_board=url_for_board, board_id=board_id,
                                              url_for_member=url_for_member, querystring=invalid_querystring_for_member)
        assert response.status_code == 400
        assert response.json()['message'] == 'invalid email address'

    def test_getting_board_members(self, member_setup):
        board_id = board.create_board_response.json()['id']
        member.get_board_member(base_url=base_url, url_for_board=url_for_board, board_id=board_id,
                                url_for_member=url_for_member)
        assert member.get_board_member_response.status_code == 200
        assert member.get_board_member_response.json()[1]['fullName'] == querystring_for_member[
            'fullName']

    def test_get_member_by_its_id(self, member_setup):
        member_id = member.create_board_member_response.json()['members'][1]['id']
        member.get_member(base_url=base_url, url_for_member=url_for_member, member_id=member_id)
        assert member.get_board_member_response.status_code == 200
        assert member.get_board_member_response.json()[1]['fullName'] == querystring_for_member[
            'fullName']

    # def test_test_avatar_creation(self, member_setup):
    #     member_id = member.create_board_member_response.json()['members'][1]['id']
    #     reponse = member.creating_avatar_for_member(base_url=base_url, url_for_member=url_for_member,
    #                                                 member_id=member_id,
    #                                                 url_for_avatar=url_for_avatar,
    #                                                 querystring=querystring_for_member_avatar)
    #     print(reponse.json())
    #     print(member.member_avatar_response.json())

