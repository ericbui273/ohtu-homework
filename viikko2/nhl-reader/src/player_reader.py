import requests
from player import Player

class PlayerReader:# pylint: disable=too-few-public-methods
    def __init__(self, url):
        self.file = requests.get(url,timeout=10).json()

    def get_players(self):
        players = []

        for player in self.file:
            players.append(Player(player))

        return players
