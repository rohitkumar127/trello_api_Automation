querystring_for_board = {
    "name": 'first_board'
}

querystring_for_list = {
    "name": 'first_list',
    "idBoard": 0
}

querystring_for_cards = {
    "name": "first_card",
    "idList": 0
}
querystring_for_label = {
    "name": "new_label",
    "color": "blue",
    "idBoard": 0,
}
querystring_for_updated_label_name = {
    "value": "updated_label"
}

querystring_for_member = {"email": "saurabh.raj@hashedin.com", "fullName": "Saurabh Raj", "type": "normal"}
invalid_querystring_for_member = {"fullName": "Rohit Kumar", "type": "normal"}
querystring_for_get_label = {"fields": "all"}
base_url = 'https://api.trello.com/1/'

url_for_board = "boards/"
first_board_name = 'board'
board_updated_name = 'testing'
url_for_list = 'lists/'
first_list_name = "first_list"
updated_list_name = 'updated_list'
first_card_name = 'first_card'
url_for_cards = 'cards/'
updated_card_name = 'updated_card'
invalid_board_url = 'beards/'
invalid_card_url = 'cords/'
url_for_member = '/members'
invalid_card_id = '123456'
getting_from_members = 'members/'
url_for_avatar = '/avatar'
querystring_for_member_avatar = {"file": "/home/rohit/Desktop/avatar.png"}
url_for_label = 'labels/'
url_to_update_label_name = '/name'
url_for_notifications = '/notifications/'
querystring_to_set_notification_status_as_unread = {"unread": "true"}
