from jsonpath import jsonpath

from api.api_corp_tag import CorpTap


class JsonPath:
    def get_corp_tag_id(self, path):
        r = CorpTap().get_corp_tag_list()
        try:
            id = jsonpath(r.json(), path)[0]["id"]
            return id
        except:
            pass


# if __name__ == '__main__':
#     id = JsonPath().get_corp_tag_id("$.[?(@.name=='小王八')]")
#     print(id)
