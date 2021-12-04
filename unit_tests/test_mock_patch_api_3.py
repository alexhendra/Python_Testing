from unittest import mock, TestCase

from app import facebook_svc

class TestApi(TestCase):
    # initial setup
    def setUp(self) -> None:
        self.patcher = mock.patch('app.facebook_svc.get_data', return_value='alex')
        self.patcher.start()
    
    def test_external_api(self):
        print('==== TESTCASE-test_external_api ====')
        self.assertEqual(facebook_svc.call_facebook_api(), 'alex')
    
    # close or dispose test case
    def tearDown(self) -> None:
        self.patcher.stop()