import datetime
import json

import requests


class DingRobot:
    def __init__(self):
        self.allure = "http://Jenkins55:4s155316@8.129.214.240:9000/job/AutoApi/allure/widgets/suites.json"
        self.ding = "https://oapi.dingtalk.com/robot/send?access_token=47efdf9004537b4951d33a55488e62975cd91fadb18c8acdd195ad6b9a942373"
        self.error = self.get_allure_error()

    def get_allure_error(self):
        jenkins_data = requests.get(self.allure).json()
        case_error = jenkins_data["items"][0]["statistic"]["failed"]
        return case_error

    def send_report(self):
        if self.error > 0:
            headers = {"Content-Type": "application/json;charset=utf-8"}
            content = {
                "msgtype": "link",
                "link": {
                    "text": "账号Jenkins55,密码4s155316",
                    "title": "，" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "picUrl": "",
                    "messageUrl": "http://Jenkins55:4s155316@8.129.214.240:9000/job/AutoApi/allure/"
                }
            }
            requests.post(self.ding, headers=headers, data=json.dumps(content))
        else:
            print('无报错')


if __name__ == '__main__':
    DingRobot().send_report()
