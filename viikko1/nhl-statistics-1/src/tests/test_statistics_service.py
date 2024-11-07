import unittest
from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
                Player("Semenko", "EDM", 4, 12),
                Player("Lemieux", "PIT", 45, 54),
                Player("Kurri", "EDM", 37, 53),
                Player("Yzerman", "DET", 42, 56),
                Player("Gretzky", "EDM", 35, 89),
                ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_with_existing_name(self):
        result = self.stats.search("Semenko")
        self.assertEqual(result.name, "Semenko")

    def test_search_with_missing_name(self):
        result = self.stats.search("Potato")
        self.assertIsNone(result)

    def test_team_with_existing_team(self):
        result = self.stats.team("EDM")
        self.assertEqual(len(result), 3)
        for player in result:
            self.assertEqual(player.team, "EDM")

    def test_top_without_sorter(self):
        result = self.stats.top(3)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].name, "Gretzky")
        self.assertEqual(result[1].name, "Lemieux")
        self.assertEqual(result[2].name, "Yzerman")

    def test_top_by_points(self):
        result = self.stats.top(3, SortBy.POINTS)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].name, "Gretzky")
        self.assertEqual(result[1].name, "Lemieux")
        self.assertEqual(result[2].name, "Yzerman")

    def test_top_by_goals(self):
        result = self.stats.top(3, SortBy.GOALS)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].name, "Lemieux")
        self.assertEqual(result[1].name, "Yzerman")
        self.assertEqual(result[2].name, "Kurri")

    def test_top_by_assists(self):
        result = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].name, "Gretzky")
        self.assertEqual(result[1].name, "Yzerman")
        self.assertEqual(result[2].name, "Lemieux")

    def test_top_by_nonexisting_option(self):
        result = self.stats.top(3, None)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].name, "Gretzky")
        self.assertEqual(result[1].name, "Lemieux")
        self.assertEqual(result[2].name, "Yzerman")
