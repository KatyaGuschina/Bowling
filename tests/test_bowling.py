# coding: UTF-8

import unittest

from bowling.game import Game


class BowlingTest(unittest.TestCase):

    def test_score(self):
        SCORE_VARIANTS = {
            "8/9-X X 6/4/X 8-X XXX": 194,
            '--------------------': 0,
            '-----1------1-------': 2,
            'XXXXXXXXXXXX': 300,
            "1/1/1/1/1/1/1/1/1/1/1/1": 110,
            '7-7-7-7-7-7-7-7-7-7-': 70,
            'X7/15X-88/-6XXXXX': 169,
            'X7/9-X-88/-6XXX81': 167,
            }
        for k, v in SCORE_VARIANTS.items():
            game = Game(k)
            self.assertEqual(max(game.get_frame_result()), v)
