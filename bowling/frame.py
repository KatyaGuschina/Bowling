# coding: UTF-8

from game import my_logger, MAX_RESULT
from bowling.throw import Throw

#MAX_RESULT = 10
class Frame:

    def __init__(self, string, first_throw, second_throw=0):
        self.string = string
        self.first_throw = Throw(self, first_throw)
        self.second_throw = Throw(self, second_throw)
        self.next_frame = None

    @property
    def strike(self):
        return self.first_throw.knocked_off == MAX_RESULT

    @property
    def spare(self):
        return not self.strike and self.first_throw.knocked_off + self.second_throw.knocked_off == MAX_RESULT

    def get_total_score(self):
        score = self.first_throw.knocked_off
        score += self.second_throw.knocked_off
        if self.strike:
            score += self.next_frame.first_throw.knocked_off
            score += self.next_frame.first_throw.next_throw.knocked_off

        if self.spare:
            score += self.next_frame.first_throw.knocked_off
        my_logger.debug(u'РћР±С‰РёР№ СЃС‡РµС‚ Р±СЂРѕСЃРєР° {}'.format(score))
        return score
