import requests
from player import Player


class PlayerReader:
    def __init__(self, url):
        response = requests.get(url).json()
        self.players = [Player(player_dict) for player_dict in response]

    def get_players(self):
        return self.players
