from io import BytesIO
import unittest
import qrcode
import sys
sys.path.append(r'C:\CODE\mc_2023_algorythm\qr_server\http')
from HttpRequest import HttpRequest

class HttpTest(unittest.TestCase):
    def test_parse_req_msg(self):
        url = 'get /qr?data=www.naver.com&user=hmd http/1.1 \n\n'
        request = HttpRequest(url.encode('utf-8'))
        print(request)