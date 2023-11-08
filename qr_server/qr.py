import qrcode
from io import BytesIO

class QR:
    @staticmethod
    def generate(self, data):
        img = qrcode.make(data)
        type(img)
        bytes = BytesIO()
        img.save(bytes)
        bytes.seek(0)
        return bytes.read()
        