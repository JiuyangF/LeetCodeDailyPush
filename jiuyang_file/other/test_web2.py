import requests
from multiprocessing import Pool

headers_v1 = {

    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Content-Length": "46",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "tgw_l7_route=4ed04efd1969357f144e2696012a8c35; laravel_session=eyJpdiI6ImhpTnh5eVRPR1wvVmlUWHVSTHZ1cHZnPT0iLCJ2YWx1ZSI6IllBK2g0TU9rTnR4WGtGeklIdWIyRTZMTGVZb1Rta1lDMkZrUXBRSzdzY3hveERJYlN4UWpwMmJ4MzBFY0kzVnhBZlhwVWxJOHNBanVUc1NkeEFnZnhBPT0iLCJtYWMiOiIwN2E1MDlkOWEyNmJiMDJmYTdjZWMzNzhjODQwNTk4MDNkMTU4NTI2YWZiNzFiNmU5ZjY5ZGEwZTllMjk5OWIxIn0%3D",
    "Host": "pc-shop.xiaoe-tech.com",
    "Origin": "https://pc-shop.xiaoe-tech.com",
    "Referer": "https://pc-shop.xiaoe-tech.com/appti1qD2S44049/video_details?id=v_5b50141c84d52_4nv97X1U",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}


def mission(url, n):
    print('*****')
    response = requests.get(url, headers=headers_v1)
    print('-----', response)
    f = open("./1/%03d.ts" % n, "wb")
    f.write(response.content)
    f.close()
    print("%03d.ts OK..." % n)


if __name__ == "__main__":
    url = 'https://vod2.xiaoe-tech.com/9764a7a5vodtransgzp1252524126/0b893d0a5285890780600972180/drm/v.f230.ts?start=45713680&end=46188383&type=mpegts&t=5be3db30&us=758323&sign=fa2c1bf5523f39e0f689a425f309f893'
    url = 'https://vod2.xiaoe-tech.com/9764a7a5vodtransgzp1252524126/0b893d0a5285890780600972180/drm/v.f230.m3u8?t=5be3db30&us=758323&sign=fa2c1bf5523f39e0f689a425f309f89'
    mission(url, 1)
    # pool = Pool(20)
    # for n in range(1, 38):
    #     url = "https://vod2.xiaoe-tech.com/9764a7a5vodtransgzp1252524126/0b893d0a5285890780600972180/drm/v.f230.ts?start=45713680&end=46188383&type=mpegts&t=5be3db30&us=758323&sign=fa2c1bf5523f39e0f689a425f309f893"
    #     pool.apply_async(mission, (url, n))
    # pool.close()
