import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_returns_player_when_name_matches(self):
        search_result = self.stats.search("Semenko")
        self.assertEqual(f"{search_result}", "Semenko EDM 4 + 12 = 16")

    def test_search_returns_none_when_name_is_not_found(self):
        self.assertIsNone(self.stats.search("Mimi"))

    def test_team_returns_players_of_requested_team(self):
        players = "\n".join([f"{player}" for player in self.stats.team("EDM")])
        compare = "Semenko EDM 4 + 12 = 16\nKurri EDM 37 + 53 = 90\n" \
                  "Gretzky EDM 35 + 89 = 124"
        self.assertEqual(players, compare)

    def test_team_returns_empty_list_when_team_is_not_found(self):
        self.assertEqual(self.stats.team("No team"), [])

    def test_top_returns_empty_list_when_number_is_negative(self):
        self.assertEqual(self.stats.top(-1), [])

    def test_top_returns_three_players_with_best_points(self):
        value = "\n".join([f"{player}" for player in self.stats.top(2, SortBy.POINTS)])
        compare ="Gretzky EDM 35 + 89 = 124\nLemieux PIT 45 + 54 = 99\n" \
                 "Yzerman DET 42 + 56 = 98"
        self.assertEqual(value, compare)

    def test_top_returns_two_players_with_best_goals(self):
        value = "\n".join([f"{player}" for player in self.stats.top(1, SortBy.GOALS)])
        compare = "Lemieux PIT 45 + 54 = 99\nYzerman DET 42 + 56 = 98"
        self.assertEqual(value, compare)

    def test_top_returns_two_players_with_best_assists(self):
        value = "\n".join([f"{player}" for player in self.stats.top(1, SortBy.ASSISTS)])
        compare = "Gretzky EDM 35 + 89 = 124\nYzerman DET 42 + 56 = 98"
        self.assertEqual(value, compare)