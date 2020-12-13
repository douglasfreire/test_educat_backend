import requests


class TestStudent:
    headers = {'Content-Type': 'application/json'}
    url_base_student = 'http://127.0.0.1:8000/students/'

    def test_get_students(self):
        students = requests.get(url=self.url_base_student, headers=self.headers)
        assert students.status_code == 200

    def test_get_student(self):
        student = requests.get(url=f'{self.url_base_student}5/', headers=self.headers)

        assert student.status_code == 200
