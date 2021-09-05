from api.api_department import Department


class TestDepartment:
    def setup_class(self):
        self.department = Department()

    def test_department_list(self):
        r = self.department.department_list([])
        assert r.status_code == 200


