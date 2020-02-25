from config import trello
from logs.logging_setup import *


class NotificationElements:
    def __init__(self):
        pass

    def get_notifications(self, base_url, url_for_notification, notification_id):
        url = base_url + url_for_notification + notification_id
        response = trello.get(url)
        self.get_notification_response = response

    def update_notifications(self, base_url, url_for_notification, notification_id, querystring):
        url = base_url + url_for_notification + notification_id
        response = trello.put(url, params=querystring)
        self.update_notification_response = response


notification = NotificationElements()
