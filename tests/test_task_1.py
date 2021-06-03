from odoo.tests import HttpCase
from ..controllers import task_1
from ..controllers import task_2


class MyTest(HttpCase):
    def test_login_api(self):
        res = self.url_open('/trust/login?user_name=admin&password=admin').read()
        self.assertEqual(res, True)

