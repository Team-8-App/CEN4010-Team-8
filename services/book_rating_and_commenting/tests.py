# test_BookRatings.py
import json
from flask_testing import TestCase
import unittest
from unittest.mock import patch, MagicMock
from BookRatings_api import app


def create_app():
    app.config['TESTING'] = True
    return app


class TestApp(TestCase):

    @patch('your_module.mysql.connector.connect')
    def test_create_rating(self, mock_connect):
        # Mocking the database connection
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor

        # Your payload
        payload = {
            "book_id": 1,
            "user_id": 1,
            "rating": 5
        }

        # Making post request and getting response
        response = self.client.post('/ratings',
                                    data=json.dumps(payload),
                                    content_type='application/json')

        # Asserting response code
        self.assert200(response)

        # Asserting response data
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data["message"], "Rating created successfully")

        # Additional assertions on database interactions can be done here if needed
        mock_cursor.execute.assert_called_once()


# This allows us to run our tests using the typical `python -m unittest discover` command
if __name__ == '__main__':
    unittest.main()
