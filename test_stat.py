import pytest
from mock import patch, call
import mock
import web_presence
import unittest
import send_information
import web_presence
from pprint import pprint
from flask import Flask


class TestInfo(unittest.TestCase):

    def setUp(self):
        web_presence.app.config['TESTING'] = True
        self.app = web_presence.app.test_client()


    #create mock objects with patch
    @patch('web_presence.Info')
    @patch('web_presence.UUIDGenerator')
    def test_index(self, mock_send_info, mock_uuid_gen):
        #Set up the test

        mock_uuid_gen.get_uuid.return_value = 'test_string'
        user_agent = 'Chrome !'
        user_address = 'UserAddress' 

        # Run the test
        self.app.get('/index',
                environ_base={'HTTP_USER_AGENT': user_agent,
                    'REMOTE_ADDR': user_address})

        # Verify What Happened
        test_calls = [call('user_id', param='test_string'),
                call('ua_device', param='Other'),
                call('ua_browser', param='Other'),
                call('status_stat', param=200),
                call('users_stat')]
        test_calls == mock_send_info.send_info.mock_calls       

if __name__ == '__main__':
    unittest.main()


