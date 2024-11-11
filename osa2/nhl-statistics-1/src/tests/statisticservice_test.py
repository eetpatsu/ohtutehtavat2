import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_loytaa_pelaajan(self):
        self.assertEqual(self.stats.search("Kurri").name, "Kurri")

    def test_search_ei_loyda_pelaajaa(self):
        self.assertEqual(self.stats.search("Paavo"), None)

    def test_team_loytaa_pelaajat(self):
        self.assertEqual(self.stats.team("EDM")[2].name, "Gretzky")

    def test_top_loytaa_n_parasta(self):
        self.assertEqual(self.stats.top(3)[2].name, "Yzerman")