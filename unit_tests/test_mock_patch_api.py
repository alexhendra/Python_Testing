from unittest import mock, TestCase

from app import facebook_svc, google_svc, data

class TestAPI(TestCase):

    @mock.patch('app.google_svc.get_data')
    def test_google_api(self, mock_google):
        print('==== TESTCASE-test_google_api ====')
        mock_google.return_value='alex'
        self.assertEqual(google_svc.call_google_api(), 'alex')


    