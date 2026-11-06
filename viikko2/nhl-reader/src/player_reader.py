import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.file = requests.get(url).json()

    def get_players(self):
        players = []

        for player in self.file:
            players.append(Player(player))

        return players

    