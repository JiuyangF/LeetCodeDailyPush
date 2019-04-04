# -*- coding: utf-8 -*-
# @Time    : 2019-03-29 4:00 PM
# @Author  : jiuyang
# @File    : file_write.py

import datetime
import json
import os
import time
import random


class HiveClient(object):
    def __init__(self, env):
        """
        create connection to hive server2
        """
        self.conn = hive.connect(**HiveHost[env])

    def query(self, sql):
        """
        query
        """
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetch()

    def close(self):
        """
        close connection
        """
        self.conn.close()

    def query_date_ad_dot_data(self, date, time):
        """
        查询某天的全部广告打点数据
        :param date:  要查询的日期
        :return:
        """
        hive1 = """select * from view_applog WHERE date='{}' and time like '{}%' and actioncode in {} ORDER by time""" \
            .format(date, time, ActionCode)
        # hive1 = '''select * from view_applog WHERE date='2019-03-26' ORDER by time limit 5'''
        # print(hive1)
        with self.conn.cursor() as cursor:
            cursor.execute(hive1)
            return cursor.fetchall()


class HiveClass:
    def __init__(self, value):
        self.value = value


class HiveConsumer(object):
    def __init__(self, env, date):
        # super().__init__(env)
        # self.data_str_list = self.cal_hive_date()
        self.date_str = date
        # self._consumer = self.date_consumer(date)

    @property
    def consumer(self):
        return self.hive_file_reader()

    def cal_hive_date(self):
        """获取需要hive数据的日期列表"""
        data_str_list = []
        date = HiveStartDate
        while date <= HiveEndDate:
            date_str = date.strftime("%Y-%m-%d")
            data_str_list.append(date_str)
            date = date + datetime.timedelta(1)
        return data_str_list

    def hive_file_reader(self):
        obj = datetime.datetime.strptime(self.date_str, '%Y-%m-%d')
        sleep_time = 0
        while True:
            q_date = obj.strftime('%Y-%m-%d')
            file_name = 'midas_data/midas-ctr-%s.hive' % q_date
            if not os.path.exists(file_name):
                if sleep_time >= 5:
                    return
                time.sleep(3)
                sleep_time += 1
                continue

            sleep_time = 0
            f = open(file_name, 'r')
            print('op*' * 20, file_name)
            for line in f.readlines():
                yield json.loads(line)
            f.close()
            os.unlink(f.name)
            obj += datetime.timedelta(1)

    def hive_file_writer(self):
        obj = datetime.datetime.strptime(self.date_str, '%Y-%m-%d')
        while True:
            q_date = obj.strftime('%Y-%m-%d')
            # 改名
            f = open('midas_data/midas-ctr-tmp.hive', 'a')
            for hour in range(6):
                if hour < 10:
                    hour_str = '0%s:' % str(hour)
                else:
                    hour_str = '%s:' % str(hour)
                # now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # print(f.name, now_time)
                # one_hour_data = self.query_date_ad_dot_data(q_date, hour_str)
                one_hour_data = [
                    ['04:59:55', '44712328', 'androidRCTeacher', '4118', 'baidu_mobile', 'banner_dj_bg', '', '',
                     'Mi_Note_3', '8.1.0', '867392034412042', '{"adId":"2017","event":"2"}', '2', '2019-03',
                     '2019-03-03'],
                    ['04:59:56', '39176100', 'androidRCTeacher', '4111', 'knowbox', 'banner_dj_bg', '', '',
                     'vivo_X9s_L', '7.1.2', '866698037014572', '{"adId":"2017","event":"2"}', '2', '2019-03',
                     '2019-03-03'],
                    ['04:59:56', '9775375', 'androidRCTeacher', '4118', 'xiaomi', 'banner_dj_bg', '', '', 'MI_6X',
                     '8.1.0', '867194042637218', '{"adId":"2322","event":"2"}', '2', '2019-03', '2019-03-03'],
                    ['04:59:58', '44712328', 'androidRCTeacher', '4118', 'baidu_mobile', 'banner_dj_bg', '', '',
                     'Mi_Note_3', '8.1.0', '867392034412042', '{"adId":"2322","event":"2"}', '2', '2019-03',
                     '2019-03-03'],
                    ['04:59:58', '39176100', 'androidRCTeacher', '4111', 'knowbox', 'banner_dj_bg', '', '',
                     'vivo_X9s_L', '7.1.2', '866698037014572', '{"adId":"2322","event":"2"}', '2', '2019-03',
                     '2019-03-03'],
                    ['04:59:58', '60422845', 'androidNewParent', '4041', 'huawei', 'banner_dj_bg', '', '', 'LLD-AL10',
                     '8.0.0', '868671034167048', '{"adId":"2816","event":"2"}', '2', '2019-03', '2019-03-03'],
                    ['04:59:58', '9775375', 'androidRCTeacher', '4118', 'xiaomi', 'banner_dj_bg', '', '', 'MI_6X',
                     '8.1.0', '867194042637218', '{"adId":"2322","event":"2"}', '2', '2019-03', '2019-03-03'],
                    ['04:59:58', '15220566', 'androidRCStudent', '4009', 'knowbox', 'banner_dj_bg', '', '', 'DOOV_A10',
                     '6.0', '863170008963909', '{"adId":"2199","event":"2"}', '2', '2019-03', '2019-03-03']]
                time.sleep(random.randint(0, 1))
                if not one_hour_data:
                    return
                for line in one_hour_data:
                    f.write(json.dumps(line) + '\n')

            f.close()
            os.rename('midas_data/midas-ctr-tmp.hive', 'midas_data/midas-ctr-%s.hive' % q_date)
            obj += datetime.timedelta(1)


if __name__ == '__main__':
    date = '2019-03-01'
    hc = HiveConsumer('test', date)
    # hc.hive_file_reader()
    for line in hc.consumer:
        print(line)
