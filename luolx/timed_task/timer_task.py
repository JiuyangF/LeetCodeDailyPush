# -*- coding: utf-8 -*-
# Created by linxin on 2018/11/13
# Copyright (c) 2018 linxin. All rights reserved.

import os
import datetime
import threading


def main_work():
    print(os.getpid(), threading.current_thread().name, "doing main work......", datetime.datetime.now())

    # 循环调用
    run_timed_task()

# ----------------------------------------------------------------------
def seconds_to_tomorrow(st='03:00:00'):
    """"""
    # 获取现在时间
    now_time = datetime.datetime.now()
    # 获取明天时间
    next_time = now_time + datetime.timedelta(days=+1)
    n_year = next_time.date().year
    n_month = next_time.date().month
    n_day = next_time.date().day
    # 获取明天3点时间
    next_time = datetime.datetime.strptime('{}-{}-{} {}'.format(n_year, n_month, n_day, st), "%Y-%m-%d %H:%M:%S")

    # 获取距离明天3点时间，单位为秒
    span_seconds = (next_time - now_time).total_seconds()
    print('获取距离明天3点的时间（单位：秒）', span_seconds)
    return span_seconds


# ----------------------------------------------------------------------
def run_timed_task():
    """"""
    # 定时器,参数为(多少时间后执行，单位为秒，执行的方法)
    # timer_task = threading.Timer(seconds_to_tomorrow(), main_work)
    timer_task = threading.Timer(3, main_work)
    # timer_task.start() # 新开一个线程
    timer_task.run()   # 在主线程中执行



run_timed_task()
