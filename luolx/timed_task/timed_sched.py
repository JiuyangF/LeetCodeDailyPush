# -*- coding: utf-8 -*-
# Created by linxin on 2018/11/13
# Copyright (c) 2018 linxin. All rights reserved.


import time, os, sched


########################################################################
class SchedTask(object):
    """这是SchedTask"""

    scedule = sched.scheduler(time.time, time.sleep)

    def __init__(self):
        """"""
        pass

    # ----------------------------------------------------------------------
    def perform_command(self, cmd, inc):
        """"""
        self.scedule.enter(inc, 0, self.perform_command, (cmd, inc))
        os.system(cmd)

    # ----------------------------------------------------------------------
    def timing_exe(self, cmd, inc=60):
        """"""
        self.scedule.enter(inc, 0, self.perform_command, (cmd, inc))
        self.scedule.run()


if __name__ == '__main__':
    print('show time after 10 seconds')
    t = SchedTask()
    t.timing_exe('date', 3)

