from api.base_api import BaseApi


class Department(BaseApi):
    def department_create(self, name):
        pass

    def department_list(self, id):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/list",
            "params": {"access_token": self.wework, "id": id},
        }
        return self.send(data)

    def department_update(self):
        pass

    def department_delete(self):
        pass
