from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        top_players = list(filter(lambda x: x.nationality == nationality, self.players))
        top_players.sort(key=lambda x: x.assists+x.goals, reverse=True)

        return top_players

    def nationality_list(self):
        nationality = set()
        for player in self.players:
            if player.nationality not in nationality:
                nationality.add(player.nationality)

        return list(nationality)