from api.base_api import BaseApi


class User(BaseApi):
    def user_create(self):
        pass

    def user_get(self, userid):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params": {"access_token": self.wework, "userid": userid}
        }
        return self.send(data)

    def user_update(self, userid, alias):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/update",
            "params": {"access_token": self.wework},
            "json": {
                "new_userid": userid,
                "alias": alias
            }
        }
        return self.send(data)

    def user_delete(self):
        pass
