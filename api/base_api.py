import json
import re

import requests


class BaseApi:
    def __init__(self):
        self.wework = self.gettoken()

    def gettoken(self):
        # todo:获取 access_token
        corpid = "ww9d7346c103e1fee0"
        corpsecret = "NhSVPKpb-LXqe8FgepvNa0VOMVeuK7a7l-vvFhgrSYE"
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": corpid,
                "corpsecret": corpsecret
            }
        }
        token = self.send(data).json()['access_token']
        return token

    def send(self, kwargs):
        r = requests.request(**kwargs)
        print(json.dumps(r.json(), indent=3, ensure_ascii=False))
        return r

    def parser(self, data):
        checkout = re.sub("{|}|\'|\"|\\[|\\]| ", "", json.dumps(data, ensure_ascii=False))
        checkouts_list = re.split(":|,", checkout)
        return set(checkouts_list)


