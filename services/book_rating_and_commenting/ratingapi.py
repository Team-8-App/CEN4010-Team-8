from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Database configuration
db_configuration = {
    'host': 'ls-b2f10f0f8d1f46949bc16b2a5608934e887eb6b0.c1zf3hrzxwhy.us-east-2.rds.amazonaws.com',
    'user': 'team_8',
    'password': 'Ankit-Bonnie-082821!',
    'database': 'team_8',
}

# Database structures to hold book rating and comments
book_ratings = {}
book_comments = {}


# Endpoint to create a rating for a book
@app.route('/book_rating', methods=['POST'])
def book_rating():
    data = request.get_json()
    user_id = data.get('user_id')
    book_id = data.get('book_id')
    rating = data.get('rating')

    # Validate the rating between 1 and 5
    if rating < 1 or rating > 5:
        return jsonify({'error': 'Rating must be between 1 and 5'}), 400

    # Store the rating
    book_ratings[(user_id, book_id)] = rating

    return jsonify({'message': 'Rating create successfully'}), 201


# Endpoint to create a comment for a book
@app.route('/comment_book', methods=['POST'])
def comment_book():
    data = request.get_json()
    user_id = data.get('user_id')
    book_id = data.get('book_id')
    comment = data.get('comment')

    # store the comment
    if book_id not in book_comments:
        book_comments[book_id] = []
        book_comments[book_id].append({'user_id': user_id, 'comment': comment})

        return jsonify({'message': 'Comment created succesfully'}), 201


# Endpoint to retrieve comments for a book
@app.route('/comments/<int:book_id>', methods=['GET'])
def retrieve_comments(book_id):
    comments = book_comments.get(book_id, [])

    return jsonify({'comments': comments})


# Endpoint to retrieve the average rating for a book
@app.route('/average_rating/<int:book_id>', methods=['GET'])
def calculate_average_rating(book_id):
    ratings = [rating for (user_id, bid), rating in book_ratings.items() if bid == book_id]

    if not ratings:
        return jsonify({'average_rating': None})

    average_rating = sum(ratings) / len(ratings)
    return jsonify({'average_rating': average_rating})


if __name__ == '__main__':
    app.run(debug=True)
