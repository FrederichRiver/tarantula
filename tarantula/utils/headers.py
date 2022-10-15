#!/usr/bin/python3

from redis import StrictRedis
import random


s = StrictRedis(db=1,decode_responses=True)


def get_headers():
    ua = s.lrange('User-Agent', 0, 36)
    headers = []
    for item in ua:
        headers.append({"User-Agent": item})
    return headers

class RandomUserAgent(object):
    """
    声明之后每次调用__call__方法即可产生一个随机的User-Agent
    """
    def __init__(self) -> None:
        ua = s.lrange('User-Agent', 0, 36)
        self.headers = []
        for item in ua:
            self.headers.append(item)
    
    def __call__(self):
        return random.choice(self.headers)

class UserHeaders(object):
    def __init__(self) -> None:
        self.ua = RandomUserAgent()
    
    def __call__(self):
        headers = {
            "User-Agent": self.ua()
        }
        return headers
    
    def __str__(self) -> str:
        return str(self.__call__())


if __name__ == '__main__':
    header = UserHeaders()
    print(header())