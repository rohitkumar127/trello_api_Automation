from config import trello


class BoardElements:
    def __init__(self):
        self.create_board_response = 0
        self.update_board_response = 0
        self.get_board_response = 0
        self.delete_board_response = 0

    def create_board(self, base_url, url_for_board, querystring):
        url = base_url + url_for_board
        response = trello.post(url, params=querystring)
        if response.status_code > 400:
            return response
        else:
            self.create_board_response = response

    def get_board_details(self, base_url, url_for_board, board_id):
        url = base_url + url_for_board + board_id
        response = trello.get(url)
        if response.status_code > 400:
            return response
        else:
            self.get_board_response = response

    def update_board_details(self, base_url, url_for_board, board_id, querystring):
        url = base_url + url_for_board + board_id
        response = trello.put(url, params=querystring)
        if response.status_code > 400:
            return response
        else:
            self.update_board_response = response

    def delete_board(self, base_url, url_for_board, board_id):
        url = base_url + url_for_board + board_id
        response = trello.delete(url)
        if response.status_code > 400:
            return response
        else:
            self.delete_board_response = response


board = BoardElements()
