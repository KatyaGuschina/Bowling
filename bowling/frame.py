# coding: UTF-8

from bowling.game import my_logger, MAX_RESULT
from bowling.throw import Throw


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
        my_logger.debug(u'Общий счет броска {}'.format(score))
        return score

    def get_frames(self):
        res = filter(lambda x: x.strip(' '), self.string)
        line = iter(res)
        i = 0
        while line:
            i = i +1
            first = line.next()
            if first == 'X':
                if i > 9:
                    f = line.next()
                    if not f == 'X':
                        raise Exception(u'Ошибка ввода')
                    try:
                        last = line.next()
                        if not last == 'X':
                            raise Exception(u'Ошибка ввода')
                        yield ('X{}{}').format(f, last)
                    except StopIteration:
                        yield ('X{}'.format(f))
                else:
                    yield ('X')
                    continue
            if line:
                second = line.next()
            else:
                second = first
            if first:
                first = str(first)
            if second:
                second = str(second)
            if first == '/':
                raise Exception(u'Ошибка ввода')
            if second == 'X':
                raise Exception(u'Ошибка ввода')
            yield first, second
