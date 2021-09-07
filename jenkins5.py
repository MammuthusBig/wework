import requests


def get_allure():
    url = "http://jenkisn5:123456@8.129.214.240:9000/job/wework/9/allure/widgets/suites.json"
    jenkins_data = requests.get(url).json()
    case_error = jenkins_data["items"][0]["statistic"]["failed"]
    print(case_error)


if __name__ == '__main__':
    get_allure()
