from trello_pages.boards import board
from trello_pages.member import member
from utility.constants import *
import pytest
from logs.logging_setup import logger


class TestMember:
    @staticmethod
    def compare_values(actual_value, expected_value):
        try:
            assert actual_value == expected_value
            logger.debug("Test Successful")
        except AssertionError:
            logger.exception('Assertion error')
            pytest.fail('Assertion error', pytrace=True)

    @pytest.mark.post
    @pytest.mark.usefixtures("member_setup")
    def test_board_member_successful_creation(self):
        self.compare_values(member.create_board_member_response.status_code, 200)

    @pytest.mark.post
    @pytest.mark.usefixtures("member_setup")
    def test_board_member_successful_creation_by_member_name(self):
        self.compare_values(member.create_board_member_response.json()['members'][1]['fullName'],
                            querystring_for_member[
                                'fullName'])

    @pytest.mark.negative_test
    @pytest.mark.usefixtures("board_setup")
    def test_board_member_unsuccessful_creation(self):
        """creating a member without an email address will give an error saying invalid email address"""
        board_id = board.create_board_response.json()['id']
        member.create_board_member(base_url=base_url, url_for_board=url_for_board, board_id=board_id,
                                   url_for_member=url_for_member, querystring=invalid_querystring_for_member)
        self.compare_values(member.create_board_member_response.status_code, 400)

    @pytest.mark.negative_test
    @pytest.mark.usefixtures("board_setup")
    def test_board_member_unsuccessful_creation_by_message_response(self):
        """creating a member without an email address will give an error saying invalid email address"""
        board_id = board.create_board_response.json()['id']
        member.create_board_member(base_url=base_url, url_for_board=url_for_board, board_id=board_id,
                                   url_for_member=url_for_member, querystring=invalid_querystring_for_member)
        self.compare_values(member.create_board_member_response.json()['message'], 'invalid email address')

    @pytest.mark.get
    @pytest.mark.usefixtures("member_setup")
    def test_getting_board_members(self):
        board_id = board.create_board_response.json()['id']
        member.get_board_member(base_url=base_url, url_for_board=url_for_board, board_id=board_id,
                                url_for_member=url_for_member)
        self.compare_values(member.get_board_member_response.status_code, 200)

    @pytest.mark.get
    @pytest.mark.usefixtures("member_setup")
    def test_getting_board_members_verifying_by_name(self):
        board_id = board.create_board_response.json()['id']
        member.get_board_member(base_url=base_url, url_for_board=url_for_board, board_id=board_id,
                                url_for_member=url_for_member)
        self.compare_values(member.get_board_member_response.json()[1]['fullName'], querystring_for_member[
            'fullName'])

    @pytest.mark.get
    @pytest.mark.usefixtures("member_setup")
    def test_get_member_by_its_id(self):
        member_id = member.create_board_member_response.json()['members'][1]['id']
        member.get_member(base_url=base_url, url_for_member=getting_from_members, member_id=member_id)
        self.compare_values(member.get_board_member_response.json()['fullName'], querystring_for_member[
            'fullName'])

    @pytest.mark.get
    @pytest.mark.usefixtures("member_setup")
    def test_get_member_notifications(self):
        member_id = member.create_board_member_response.json()['members'][0]['id']
        member.get_member_notifications(base_url=base_url, url_for_member=getting_from_members,
                                        member_id=member_id,
                                        url_for_notifications=url_for_notifications)
        print(member.get_member_notifications_response.json())
        self.compare_values(member.get_member_notifications_response.status_code, 200)


