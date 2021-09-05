from api.api_user import User


class TestUser:
    def setup_class(self):
        self.user = User()

    def test_user_get(self):
        r = self.user.user_get('SHLR')
        assert r.status_code == 200
        assert r.json()['name'] == "斯卡蒂"


