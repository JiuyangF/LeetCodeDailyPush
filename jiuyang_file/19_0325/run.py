# -*- coding: utf-8 -*-
# @Time    : 2019-03-25 11:54 AM
# @Author  : jiuyang
# @File    : run.py
import datetime

class DataWindow:
    def __init__(self, start, periods=10):

        if start is not None:
            start = datetime.datetime.now()
        self.start = start

        self.periods = periods
        self.end_time = 0

    def time_wide(self):
        return self.start_time - self.end_time




def time_window(start_time, periods):
    end_time = start_time + periods
    time_wide = end_time - start_time
    now_time =
    if time_wide <= periods:
        print('宽度不够不做处理')

    if


if __name__ == '__main__':
    f = open('test.txt', 'r')
    fd = f.read()
