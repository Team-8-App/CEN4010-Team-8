import unittest
import json
from .book_api import app

class TestBook(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_books(self):
        response = self.app.get('/books?get=books')
        self.assertEqual(response.status_code, 200)

        # Test case to retrieve list of books by genre

    def test_get_books_by_genre(self):
        response = self.app.get('/books?genre=Fiction')
        self.assertEqual(response.status_code, 200)
        books = json.loads(response.data)
        for book in books:
            self.assertEqual(book['genre'], 'Fiction')

    # Test case to retrieve list of top sellers
    def test_get_top_sellers(self):
        response = self.app.get('/books?top_sellers=10')
        self.assertEqual(response.status_code, 200)
        books = json.loads(response.data)
        self.assertTrue(len(books) <= 10)
        if len(books) > 1:
            self.assertTrue(books[0]['copies_sold'] >= books[1]['copies_sold'])

    # Test case to retrieve list of books with a particular rating and higher
    def test_get_books_by_rating(self):
        response = self.app.get('/books?min_rating=4')
        self.assertEqual(response.status_code, 200)
        books = json.loads(response.data)
        for book in books:
            self.assertTrue(book['rating'] >= 4)

    # Test case to retrieve list of discounted books by publisher
    def test_get_discounted_books_by_publisher(self):
        response = self.app.get('/books?publisher=Publisher&publisher_discount=True')
        self.assertEqual(response.status_code, 200)
        books = json.loads(response.data)
        for book in books:
            self.assertEqual(book['publisher'], 'Publisher')
            self.assertTrue(book['discount'] > 0)

if __name__ == '__main__':
    unittest.main()
