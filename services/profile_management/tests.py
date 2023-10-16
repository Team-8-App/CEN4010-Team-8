import json
import unittest
from .profile_management_api import app

class TestUserProfile(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_user_profile_sory_by_username(self):
        # Send a GET request to /user-profile with a username filter
        response = self.app.get('/user-profile?sort_by=username')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Parse the JSON response data
        user_profiles = json.loads(response.data)
        self.assertEqual(user_profiles[0]['username'], '1697429176')

    def test_get_user_profile_invalid_sort_by_user_id(self):
        # Send a GET request to /user-profile with a username filter
        response = self.app.get('/user-profile?sort_by=user_id')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Parse the JSON response data
        user_profiles = json.loads(response.data)
        self.assertEqual(user_profiles[0]['user_id'], 0)

    def test_get_user_profile_invalid_sort(self):
        # Send a GET request to /user-profile with a username filter
        response = self.app.get('/user-profile?sort_by=none')
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Parse the JSON response data
        user_profiles = json.loads(response.data)
        self.assertEqual(user_profiles['error'], 'Invalid sort column')

    def test_post_and_delete_user_profile(self):
        # Send a POST request to create a new user profile
        user_data = {
            'username': 'testuser25',
            'password': 'testuser25',
            'name': 'testuser25',
            'email_address': 'testuser25@example.com',
            'home_address': 'testuser25',
            'user_id': 25
        }
        response = self.app.post('/user-profile', json=user_data)

        # Check if the response status code is 200 (OK) or a success status code
        self.assertEqual(response.status_code, 200)

        # Parse the JSON response data and check for a success message
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'], 'User created successfully')

        # DELETE THE NEW USER
        get_response = self.app.delete(f"/user-profile/{user_data['user_id']}")


    def test_patch_user_profile(self):
        # Send a PATCH request to update an existing user profile
        user_id = 123  # Assuming this user ID exists in your database
        user_data = {
            'username': 'Updated Name',
            'home_address': 'Updated Address'
        }
        response = self.app.patch(f'/user-profile/{user_id}', json=user_data)

        # Check if the response status code is 200 (OK) or a success status code
        self.assertEqual(response.status_code, 200)

        # Parse the JSON response data and check for a success message
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'], f'User with ID {user_id} updated successfully')
        user_data = {
            'username': 'newuser',
            'home_address': '123 New Street'
        }
        response = self.app.patch(f'/user-profile/{user_id}', json=user_data)
        response_data = json.loads(response.data)

    def test_get_credit_cards_by_user_id(self):
        # Send a GET request to retrieve credit cards by user_id
        user_id = 1  # Replace with a valid user_id
        response = self.app.get(f'/credit-card?user_id={user_id}')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Parse the JSON response data and check its content
        credit_cards = json.loads(response.data)

        # Add assertions to verify the content of the credit card data based on your application's structure
        self.assertTrue(isinstance(credit_cards, list))
        for card in credit_cards:
            self.assertEqual(card['user_id'], user_id)

    def test_get_credit_cards_missing_user_id(self):
        # Send a GET request without a user_id parameter
        response = self.app.get('/credit-card')

        # Check if the response status code is 400 (Bad Request) indicating a missing user_id
        self.assertEqual(response.status_code, 400)

        # Parse the JSON response data and check for an error message
        response_data = json.loads(response.data)
        self.assertEqual(response_data['error'], 'User ID is required')

    def test_post_credit_card(self):
        # Send a POST request to add a new credit card
        card_data = {
            'user_id': 1697429176,  # Replace with a valid user_id
            'card_number': '1234567890123456',
            'expiry_date': '12/24',
            'cvv': '123',
            'card_holder_name': 'Test'
        }
        response = self.app.post('/credit-card', json=card_data)

        # Check if the response status code is 201 (Created)
        self.assertEqual(response.status_code, 201)

        # Parse the JSON response data and check for a success message
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'], 'Card added')
        response = self.app.delete(f"/credit-card/{card_data['user_id']}")

if __name__ == '__main__':
    unittest.main()
