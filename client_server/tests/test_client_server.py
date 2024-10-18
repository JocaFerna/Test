import unittest
from client import request_server

class TestClientServer(unittest.TestCase):
    def test_client_response(self):
        request_server()  # Expecting "Hello, Client!" response

if __name__ == "__main__":
    unittest.main()