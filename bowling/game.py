# coding: UTF-8

import argparse
import logging
import texttable as tt
import sys
# from bowling.parse import Parse
from bowling.frame import Frame 

MAX_RESULT = 10
FRAMES = 10
my_logger = logging.getLogger('my')
my_logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr = logging.FileHandler('my_logger.txt')
hdlr.setFormatter(formatter)
my_logger.addHandler(hdlr)

ex = "8/9-X X 6/4/X 8-X XXX"


class Game:

    def __init__(self, string):
        self.string = string
        self.frames = list(self.parse())

    def get_frame_result(self):
        fn = 0
        for index, frame in enumerate(self.frames[:-1]):
            frame.next_frame = self.frames[index+1]
        for frame in self.frames[:FRAMES]:
            fn = fn + frame.get_total_score()
            my_logger.debug(u'Общее количество набранных очков - {}'.format(fn))
            yield fn

    def parse(self):
        res = filter(lambda x: x.strip(' '), self.string)
        line = iter(res)
        i = 0
        while line:
            i = i + 1
            first = line.next()
            s = 0
            f = first
            if first == 'X':
                yield Frame(f, 10, 0)
                continue
            elif first == '/':
                raise Exception('Ошибка ввода, первый удар не может быть spare!')
            if line:
                try:
                    second = line.next()
                    if second == 'X':
                        raise Exception('Ошибка ввода, второй удар не может быть strike!')
                    s = second
                except StopIteration:
                    s = ''
                    second = 0
            else:
                second = 0

            if first == '-':
                first = 0
            else:
                if first == '/':
                    raise Exception('Введенны некорректные данные')
                first = int(first)
            if second == '/':
                second = MAX_RESULT - first
            elif second == '-':
                second = 0
            else:
                second = int(second)
            yield Frame(f + s, first, second)

    def get_final_result(self):
        game = Game(ex)
        gen = list(game.parse())
        list_frames = [x.string for x in gen]
        try:
            ten = list_frames.pop(10)
        except IndexError:
            ten = ''
        try:
            eleven = list_frames.pop(10)
        except IndexError:
            eleven = ''
        try:
            list_frames.pop(10)
            return u'Слишком длинное значени строки'
        except IndexError:
            pass
        try:
            list_frames[9] = str(list_frames[9]) + str(ten) + str(eleven)
        except IndexError:
            return u'Слишком короткое значение строки'
        t = tt.Texttable()
        header = ['1', '2', '3', '4',  '5', '6', '7', '8', '9', '10']
        t.header(header)
        row = list_frames
        t.add_row(row)
        row = list(game.get_frame_result())
        t.add_row(row)
        t.set_chars(['-', '|', '+', '='])
        s = t.draw()

        return s


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', default=ex)
    namespace = parser.parse_args(sys.argv[1:])

    game = Game(namespace.r)
    result = game.get_final_result()

    print result

if __name__ == '__main__':
        main()
