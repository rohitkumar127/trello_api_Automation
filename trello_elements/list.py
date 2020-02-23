from config import trello


class ListElements:
    def __init__(self):
        pass

    def create_list(self, base_url, url_for_list, querystring):
        url = base_url + url_for_list
        response = trello.post(url, params=querystring)
        return response

    def get_list_details(self, base_url, url_for_list, list_id):
        url = base_url + url_for_list + list_id
        response = trello.get(url)
        return response

    def update_list_details(self, base_url, url_for_list, list_id, querystring):
        url = base_url + url_for_list + list_id
        response = trello.put(url, params=querystring)
        return response


trello_list = ListElements()
