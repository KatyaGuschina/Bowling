# coding: UTF-8


class Parse:

    def __init__(self, string):
        self.string = string

    def parse(self):
        res = filter(lambda x: x.strip(' '), self.string)
        line = iter(res)
        i = 0
        while line:
            i = i +1
            first = line.next()
            if first == 'X':
                if i > 9:
                    f = line.next()
                    try:
                        last = line.next()
                        if not f == 'X':
                            raise Exception('Ошибка ввода, так как 11 бросок не является strike, 12й бросок невозможен')
                        yield 'X{}{}'.format(f, last), ''
                    except StopIteration:
                        yield 'X{}'.format(f)
                else:
                    yield 'X', ''
                    continue
            if line:
                second = line.next()
            else:
                second = ''
            if first:
                first = str(first)
            if second:
                second = str(second)
            if first == '/':
                raise Exception('Ошибка ввода, первый удар не может быть spare!')
            if second == 'X':
                raise Exception('Ошибка ввода, второй удар не может быть strike!')
            first = str(first)
            second = str(second)
            yield first, second
