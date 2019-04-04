# -*- coding: utf-8 -*-
# @Time    : 2019-03-28 5:47 PM
# @Author  : jiuyang
# @File    : test.py
import redis


class RedisHelper(object):
    def __init__(self):
        self.__conn = redis.Redis(host='localhost')  # 连接本机，ip不用写
        self.chan_sub = 'fm104.5'

    def public(self, msg):
        self.__conn.publish(self.chan_sub, msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)  # 订阅的频道
        pub.parse_response()  # 准备好监听(再调用一次就是开始监听)
        return pub
