from trello_pages.notifications import notification
from trello_pages.member import member
from constants import *
import pytest
from logs.logging_setup import logger


class TestNotification:
    @staticmethod
    def compare_values(actual_value, expected_value):
        try:
            assert actual_value == expected_value
            logger.debug("Test Successful")
        except AssertionError:
            logger.exception('Assertion error')
            pytest.fail('Assertion error', pytrace=True)

    @pytest.mark.get
    @pytest.mark.usefixtures("member_setup")
    def test_get_member_notifications(self):
        member_id = member.create_board_member_response.json()['members'][0]['id']
        member.get_member_notifications(base_url=base_url, url_for_member=getting_from_members,
                                        member_id=member_id,
                                        url_for_notifications=url_for_notifications)
        notification_id = member.get_member_notifications_response.json()[0]['id']
        notification.get_notifications(base_url=base_url, url_for_notification=url_for_notifications,
                                       notification_id=notification_id)
        self.compare_values(notification.get_notification_response.status_code, 200)

    def test_update_notification_read_status_verify_status_code(self):
        member_id = member.create_board_member_response.json()['members'][0]['id']
        member.get_member_notifications(base_url=base_url, url_for_member=getting_from_members,
                                        member_id=member_id,
                                        url_for_notifications=url_for_notifications)
        notification_id = member.get_member_notifications_response.json()[0]['id']
        notification.update_notifications(base_url=base_url, url_for_notification=url_for_notifications,
                                          notification_id=notification_id,
                                          querystring=querystring_to_set_notification_status_as_unread)
        self.compare_values(notification.update_notification_response.status_code, 200)

    def test_update_notification_read_status_verify_unread_property(self):
        member_id = member.create_board_member_response.json()['members'][0]['id']
        member.get_member_notifications(base_url=base_url, url_for_member=getting_from_members,
                                        member_id=member_id,
                                        url_for_notifications=url_for_notifications)
        notification_id = member.get_member_notifications_response.json()[0]['id']
        notification.update_notifications(base_url=base_url, url_for_notification=url_for_notifications,
                                          notification_id=notification_id,
                                          querystring=querystring_to_set_notification_status_as_unread)
        self.compare_values(notification.update_notification_response.json()['unread'], True)
