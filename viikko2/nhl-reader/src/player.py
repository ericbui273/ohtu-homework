class Player: # pylint: disable=too-few-public-methods
    def __init__(self, player):
        self.name = player['name']
        self.nationality = player['nationality']
        self.goals = player['goals']
        self.assists = player['assists']
        self.team = player['team']

    def __str__(self):
        return f"{self.name} {self.team} {self.goals} + {self.assists} = {self.goals+self.assists}"
