import json
import unittest
from profile_management_api import app

class TestUserProfile(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_user_profile(self):
        # Send a GET request to /user-profile with a username filter
        response = self.app.get('/user-profile?username=testuser')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Parse the JSON response data
        user_profiles = json.loads(response.data)

        # You can add more specific assertions here based on your expectations
        # For example, you can check if the returned user profiles contain the expected fields.

if __name__ == '__main__':
    unittest.main()
