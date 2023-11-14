# test_BookRatings.py
import json
import unittest
from BookRatings_api import app


class TestBookRating(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_rating(self):
        response = self.app.get('/ratings?min_rating=4')
        self.assertEqual(response.status_code, 200)
        ratings = json.loads(response.data)
        for rating in ratings:
            self.assertGreaterEqual(rating['rating'], 4)

    def test_get_comment(self):
        response = self.app.get('/comments?comment=Very cool')
        self.assertEqual(response.status_code, 200)
        comments = json.loads(response.data)
        for comment in comments:
            self.assertEqual(comment['comment'], 'Very cool')

    def test_get_rating_invalid_sort_by_book_id(self):
        response = self.app.get('/ratings?sort_by=book_id')
        self.assertEqual(response.status_code, 200)
        book_ratings = json.loads(response.data)
        self.assertEqual(book_ratings[0]['book_id'], 0)

    def test_get_rating_invalid_sort(self):
        response = self.app.get('/ratings?sort_by=none')
        self.assertEqual(response.status_code, 200)
        book_ratings = json.loads(response.data)
        self.assertEqual(book_ratings['error'], 'Invalid sort column')

    def test_post_rating(self):
        user_data = {
            'user_id': 123,
            'book_id': 1,
            'rating': 3
        }
        # Test POST request
        response = self.app.post('/ratings', json=user_data)
        self.assertEqual(response.status_code, 201)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'], 'Rating created successfully')

    def test_post_comment(self):
        comment_data = {
            'user_id': 123,
            'book_id': 1,
            'comment': 'wow'
        }
        # Test POST request
        response = self.app.post('/comments', json=comment_data)
        self.assertEqual(response.status_code, 201)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'], 'Comment created successfully')


if __name__ == '__main__':
    unittest.main()
