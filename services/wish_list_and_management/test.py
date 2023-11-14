import unittest
import json
from .wishlist_api import app

class TestWishlistAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_all_wishlists(self):
        response = self.app.get(f"/user/{self.user_id}/wishlists")
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions to check the response data

    def test_create_wishlist(self):
        wishlist_data = {
            'wishlist_name': 'Test Wishlist'
        }
        response = self.app.post(f"/user/{self.user_id}/wishlist", json=wishlist_data)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions to check the response data

    def test_add_book_to_wishlist(self):
        response = self.app.post(f"/user/{self.user_id}/wishlist/{self.wishlist_id}/book/{self.book_id}")
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions to check the response data

    def test_remove_book_from_wishlist(self):
        response = self.app.delete(f"/user/{self.user_id}/wishlist/{self.wishlist_id}/book/{self.book_id}")
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions to check the response data

    def test_get_books_in_wishlist(self):
        response = self.app.get(f"/user/{self.user_id}/wishlist/{self.wishlist_id}/books")
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions to check the response data

if __name__ == '__main__':
    unittest.main()
