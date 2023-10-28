import unittest
import json
from shopping_cart_api import app


class ShoppingCartTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_retrieve_subtotal_price(self):
        user_id = 1
        response = self.app.get(f'/shopping-cart?user_id={user_id}')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)
        subtotal = sum(float(item['subtotal']) for item in data['books_in_cart'])
        self.assertEqual(data['subtotal'], subtotal)

    def test_add_book_to_cart(self):
        user_id = 1
        book_id = 1
        data = {
            'user_id': user_id,
            'book_id': book_id,
            'quantity': 1,
            'price': 19.99
        }
        response = self.app.post('/shopping-cart', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Book added to cart successfully')

    def test_retrieve_books_in_cart(self):
        user_id = 1
        response = self.app.get(f'/shopping-cart?user_id={user_id}')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)
        for item in data['books_in_cart']:
            self.assertIn('title', item)
            self.assertIn('publisher', item)

    def test_delete_book_from_cart(self):
        user_id = 1
        book_id = 1
        response = self.app.delete(f'/shopping-cart/{book_id}?user_id={user_id}')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Book deleted from cart successfully')


if __name__ == '__main__':
    unittest.main()
