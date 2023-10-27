import json
import unittest
from .book_detail_api import app

class TestBookDetailAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_book_detail(self):
        response = self.app.get('/book_detail')
        self.assertEqual(response.status_code, 200)

    def test_get_isbn(self):
        response = self.app.get('/book_detail?isbn=57887')

    def test_get_book_name(self):
        response = self.app.get('/book_detail?book_name=BookName Here')

    def test_get_description(self):
        response = self.app.get('/book_detail?description=Here is a book description')

    def test_get_price(self):
        response = self.app.get('/book_detail?price=10.99')

    def test_get_genre(self):
        response = self.app.get('/book_detail?genre=Fiction')

    def test_get_publisher(self):
        response = self.app.get('/book_detail?publisher=Insert Publisher Here')

    def test_get_year_published(self):
        response = self.app.get('/book_detail?year_published=1996')

    def test_get_copies_sold(self):
        response = self.app.get('/book_detail?copies_sold=50')

if __name__ == '__main__':
    unittest.main()