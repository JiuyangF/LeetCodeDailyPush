# -*- coding: utf-8 -*-
# Created by linxin on 2018/11/13
# Copyright (c) 2018 linxin. All rights reserved.


import schedule
import time

# ----------------------------------------------------------------------


def main_work():
    """"""
    print('main work doing......')
    time.sleep(3)


schedule.every(2).seconds.do(main_work)  # 每隔 2s 执行一次任务
schedule.every(10).minutes.do(main_work)  # 每隔十分钟执行一次任务
schedule.every().hour.do(main_work)  # 每隔一小时执行一次任务
schedule.every().day.at('10:30').do(main_work)  # 每天的10:30执行一次任务
schedule.every(5).to(10).days.do(main_work)  #
schedule.every().monday.do(main_work)  # 每周一的这个时候执行一次任务
schedule.every().wednesday.at('13:15').do(main_work)  # 每周三13:15执行一次任务

while True:
    schedule.run_pending()  # 运行所有可以运行的任务
    # time.sleep(1)
