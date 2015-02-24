# coding: UTF-8


class Throw:

    def __init__(self, frame, knocked_off):
        self.frame = frame
        self.knocked_off = knocked_off

    @property
    def next_throw(self):
        if self == self.frame.first_throw and not self.frame.strike:
            return self.frame.second_throw
        else:
            return self.frame.next_frame.first_throw