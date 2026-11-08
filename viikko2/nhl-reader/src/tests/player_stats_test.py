import unittest

from player import Player
from player_stats import PlayerStats


class StubReader: # pylint: disable=too-few-public-methods
    def get_players(self):
        return [
            Player(
                {
                    "name": "Player A",
                    "team": "EDM",
                    "goals": 20,
                    "assists": 30,
                    "nationality": "FIN",
                }
            ),
            Player(
                {
                    "name": "Player B",
                    "team": "EDM",
                    "goals": 12,
                    "assists": 15,
                    "nationality": "USA",
                }
            ),
            Player(
                {
                    "name": "Player C",
                    "team": "TOR",
                    "goals": 18,
                    "assists": 22,
                    "nationality": "FIN",
                }
            ),
            Player(
                {
                    "name": "Player D",
                    "team": "TOR",
                    "goals": 25,
                    "assists": 10,
                    "nationality": "CAN",
                }
            ),
        ]


class PlayerStatsTest(unittest.TestCase):
    def setUp(self):
        self.stats = PlayerStats(StubReader())

    def test_top_scorers_by_nationality_sorts_by_total_points(self):
        scorers = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual([player.name for player in scorers], ["Player A", "Player C"])
        self.assertEqual(scorers[0].goals + scorers[0].assists, 50)
        self.assertEqual(scorers[1].goals + scorers[1].assists, 40)

    def test_top_scorers_by_team_sorts_by_total_points(self):
        scorers = self.stats.top_scorers_by_team("EDM")

        self.assertEqual([player.name for player in scorers], ["Player A", "Player B"])
        self.assertEqual(scorers[0].goals + scorers[0].assists, 50)
        self.assertEqual(scorers[1].goals + scorers[1].assists, 27)
