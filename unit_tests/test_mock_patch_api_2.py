from unittest import mock, TestCase

from app import facebook_svc, data

class TestAPI(TestCase):

    def test_facebook_api(self):
        print('==== TESTCASE-test_facebook_api ====')
        with mock.patch('app.facebook_svc.get_data', return_value='alex'):
            self.assertEqual(facebook_svc.call_facebook_api(), 'alex')


    