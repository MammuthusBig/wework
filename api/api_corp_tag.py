from api.base_api import BaseApi


class CorpTap(BaseApi):

    # todo: 添加企业客户标签
    def add_corp_tag(self, name, **kwargs):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            "params": {"access_token": self.wework},
            "json": {
                "tag": [{'name': name}],
                **kwargs
            }
        }
        return self.send(data)

    # todo: 获取企业标签库
    def get_corp_tag_list(self, **kwargs):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            "params": {"access_token": self.wework},
            "json": {
                **kwargs
            }
        }
        return self.send(data)

    # todo: 编辑企业客户标签
    def edit_corp_tag(self, id, tag_name):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
            "params": {"access_token": self.wework},
            "json": {
                "id": id,
                "name": tag_name
            }
        }
        return self.send(data)

    # todo: 删除企业客户标签
    def del_corp_tag(self, **kwargs):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params": {"access_token": self.wework},
            "json": {
                **kwargs
            }
        }
        return self.send(data)
