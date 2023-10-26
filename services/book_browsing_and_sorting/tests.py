import json
import unittest
from .book_api import app

class TestBookBrowsingAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_books(self):
        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)

    def test_get_books_with_genre_filter(self):
        response = self.app.get('/books?genre=Science Fiction')

    def test_get_books_with_invalid_sort_by(self):
        response = self.app.get('/books?sort_by=invalid_column')

    def test_get_books_with_top_sellers(self):
        response = self.app.get('/books?top_sellers=10')

    def test_get_books_with_publisher_discount(self):
        response =  self.app.get('/books?publisher_discount=PublisherABC')

if __name__ == '__main__':
    unittest.main()