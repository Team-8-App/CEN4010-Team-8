# test_BookRatings.py
import json
from flask_testing import TestCase
import unittest
from BookRatings_api import app  # 'BookRatings_api.py' REST API code


class TestApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_create_rating(self):
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

    # More test methods...


# This allows us to run our tests using the typical `python -m unittest discover` command
if __name__ == '__main__':
    unittest.main()
