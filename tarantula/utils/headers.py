#!/usr/bin/python3

from redis import StrictRedis


s = StrictRedis(db=1,decode_responses=True)


def get_headers():
    ua = s.lrange('User-Agent', 0, 36)
    headers = []
    for item in ua:
        headers.append({"User-Agent": item})
    return headers

