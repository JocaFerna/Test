import unittest
import requests

class TestMicroservices(unittest.TestCase):
    def test_user_service(self):
        response = requests.get('http://localhost:5001/users')
        self.assertEqual(response.status_code, 200)
        self.assertIn("John Doe", response.text)

    def test_order_service(self):
        response = requests.get('http://localhost:5002/orders')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Laptop", response.text)

if __name__ == "__main__":
    unittest.main()