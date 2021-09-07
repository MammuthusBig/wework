import requests


class DingRobot:
    pass


def get_allure():
    url = "http://jenkisn5:123456@8.129.214.240:9000/job/wework/allure/widgets/suites.json"
    jenkins_data = requests.get(url).json()
    print(jenkins_data)
    # case_error = jenkins_data["items"][0]["statistic"]["failed"]
    # print(case_error)


# def send_report():
#     url = 'https://oapi.dingtalk.com/robot/send?access_token=' \
#           'a5eb6e38be242dcf3a0ceaa1035a8c3093430de8da7384bf0b710711d4885c49'
#     headers = {"Content-Type": "application/json;charset=utf-8"}
#     content = {
#         "msgtype": "link",
#         "link": {
#             "text": "这个即将发布的新版本，创始人xx称它为红树林。而在此之前，每当面临重大升级，产品经理们都会取一个应景的代号，这一次，为什么是红树林",
#             "title": "猛犸象" + "时代的火车向前开",
#             "picUrl": "",
#             "messageUrl": "https://www.baidu.com/"
#         }
#     }
#
#     response = requests.post(url, headers=headers, data=json.dumps(content))
#     print(response.text)
#     return response


if __name__ == '__main__':
    get_allure()
