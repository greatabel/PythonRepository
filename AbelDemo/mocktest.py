#coding: utf-8
import unittest


from unittest import mock
import mockclient

import colorama
from colorama import Fore, Back, Style

class TestClient(unittest.TestCase):

    def test_success_request(self):
        success_send = mock.Mock(return_value='200')
        mockclient.send_request = success_send
        self.assertEqual(mockclient.visitdouban(), '200')

    def test_fail_request(self):
        fail_send = mock.Mock(return_value='404')
        mockclient.send_request = fail_send
        self.assertEqual(mockclient.visitdouban(), '404')

class TestClient_Advanced(unittest.TestCase):

    def test_success_request(self):
        status_code = '200'
        success_send = mock.Mock(return_value=status_code)
        with mock.patch('mockclient.send_request', success_send):
            from mockclient import visitdouban
            self.assertEqual(visitdouban(), status_code)

    def test_fail_request(self):
        status_code = '404'
        fail_send = mock.Mock(return_value=status_code)
        with mock.patch('mockclient.send_request', fail_send):
            from mockclient import visitdouban
            self.assertEqual(visitdouban(), status_code)

if __name__ == '__main__':
    t = TestClient()
    t.test_success_request()
    t.test_fail_request()

    print(Fore.GREEN + '-'*20 + Fore.RESET+Back.RED+'demo2'+Back.RESET)
    
    at = TestClient_Advanced()
    at.test_success_request()
    at.test_fail_request()
