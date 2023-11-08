from io import ByteIO
import unittest
import qrcode

class QRTest(unittest.TestCase):
    def test_generate_qr(self):
        img = qrcode.make('https://www.naver.com')
        type(img)
        bytes = BytesIO()
        img.save(bytes)
        bytes.seek(0)
        print(bytes.read())
        