from config import trello


class BoardElements:
    def __init__(self):
        pass

    def create_board(self, base_url, url_for_board, querystring):
        url = base_url + url_for_board
        response = trello.post(url, params=querystring)
        return response

    def get_board_details(self, base_url, url_for_board, board_id):
        url = base_url + url_for_board + board_id
        response = trello.get(url)
        return response

    def update_board_details(self, base_url, url_for_board, board_id, querystring):
        url = base_url + url_for_board + board_id
        response = trello.put(url, params=querystring)
        return response

    def delete_board(self, base_url, url_for_board, board_id):
        url = base_url + url_for_board + board_id
        response = trello.delete(url)
        return response


board = BoardElements()
