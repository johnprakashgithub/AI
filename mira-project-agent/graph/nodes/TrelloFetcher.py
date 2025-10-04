import requests

class TrelloFetcher:
    def __init__(self, api_key, token, board_id=None, list_id=None):
        self.api_key = api_key
        self.token = token
        self.board_id = board_id
        self.list_id = list_id

    def __call__(self, state):
        # Construct Trello API URL
        if self.list_id:
            url = f"https://api.trello.com/1/lists/{self.list_id}/cards"
        elif self.board_id:
            url = f"https://api.trello.com/1/boards/{self.board_id}/cards"
        else:
            raise ValueError("Either board_id or list_id must be provided")

        # Fetch cards
        params = {
            "key": self.api_key,
            "token": self.token
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        cards = response.json()

        # Return updated state with Trello data
        return {**state, "trello_cards": cards}
