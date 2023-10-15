import json
from flask_testing import TestCase
import unittest
from unittest.mock import patch, MagicMock
from book_detail_api import app

def create_app():
    app.config['TESTING'] = True
    return app

class TestApp(TestCase):

    @patch('your_module.mysql.connector.connect')
    def test_create_detail(self, mock_connect):

        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor

        payload = {
            "isbn": "978-3-16-148410-0",
            "book_name": "Sample Book",
            "description": "This is a sample book description.",
            "price": 25.99,
            "author_id": 1,
            "genre": "Fiction",
            "publisher": "Sample Publisher",
            "year_published": 2022,
            "copies_sold": 1000
        }

        response = self.client.post('/book_detail',
                                    data=json.dumps(payload),
                                    content_type='application/json')

        self.assert200(response)

        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data["message"], "Book details created successfully")

        mock_cursor.execute.assert_called_once()

if __name__ == '__main__':
    unittest.main()