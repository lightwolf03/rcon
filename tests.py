import unittest
from models.connection import RconConnection

class UnitTests(unittest.TestCase):
    def test_1(self):
        connection = RconConnection("192.168.0.101", 28960, "04101963")
        connection.connect()
        connection.auth()
        connection.sendRaw(b"\xFF\xFF\xFF\xFFstatus\x00")
        while True:
            response = connection.response(1024)
            print(response)


if __name__ == '__main__':
    unittest.main()