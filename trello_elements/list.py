from config import trello


class ListElements:
    def __init__(self):
        self.create_list_response = 0
        self.update_list_response = 0
        self.get_list_response = 0

    def create_list(self, base_url, url_for_list, querystring):
        url = base_url + url_for_list
        response = trello.post(url, params=querystring)
        if response.status_code >= 400:
            return response
        else:
            self.create_list_response = response

    def get_list_details(self, base_url, url_for_list, list_id):
        url = base_url + url_for_list + list_id
        response = trello.get(url)
        if response.status_code >= 400:
            return response
        else:
            self.get_list_response = response

    def update_list_details(self, base_url, url_for_list, list_id, querystring):
        url = base_url + url_for_list + list_id
        response = trello.put(url, params=querystring)
        if response.status_code >= 400:
            return response
        else:
            self.update_list_response = response


trello_list = ListElements()
