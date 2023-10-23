from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'HOST_8',
    'user': 'team_8',
    'password': 'PASSWORD_8',
    'database': 'team_8'
}

# GET endpoint to retrieve books
@app.route('/books', methods=['GET'])
def get_books():
    genre_filter = request.args.get('genre')
    sort_by = request.args.get('sort_by', 'title')
    publisher_discount = request.args.get('publisher_discount')
    min_rating = request.args.get('min_rating', type=float)
    top_sellers = request.args.get('top_sellers', type=int)

    valid_sort_columns = ["title", "genre", "copies_sold", "rating", "publisher", "discount"]
    if sort_by not in valid_sort_columns:
        return jsonify({'error': 'Invalid sort column'}), 400

    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM Books WHERE 1=1"
        query_args = []

        if genre_filter:
            query += " AND genre=%s"
            query_args.append(genre_filter)

        if publisher_discount:
            query += " AND publisher=%s AND discount > 0"
            query_args.append(publisher_discount)

        if min_rating is not None:
            query += " AND rating >= %s"
            query_args.append(min_rating)

        if top_sellers is not None:
            query += " ORDER BY copies_sold DESC LIMIT %s"
            query_args.append(top_sellers)
        else:
            query += f" ORDER BY {sort_by}"

        cursor.execute(query, query_args)
        books = cursor.fetchall()

        return jsonify(books)

    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)}), 500

    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

# POST endpoint to create a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.json

    title = data.get('title')
    genre = data.get('genre')
    publisher = data.get('publisher')
    rating = data.get('rating')
    copies_sold = data.get('copies_sold', 0)
    discount = data.get('discount', 0)

    if not title or not genre or not publisher or rating is None:
        return jsonify({'error': 'Missing required fields'}), 400

    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = "INSERT INTO Books (title, genre, publisher, rating, copies_sold, discount) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (title, genre, publisher, rating, copies_sold, discount))
        conn.commit()

        return jsonify({'message': 'Book created successfully'}), 201

    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)}), 500

    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

# PUT endpoint to update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json

    title = data.get('title')
    genre = data.get('genre')
    publisher = data.get('publisher')
    rating = data.get('rating')
    copies_sold = data.get('copies_sold')
    discount = data.get('discount')

    if not title and not genre and not publisher and rating is None and copies_sold is None and discount is None:
        return jsonify({'error': 'No fields to update'}), 400

    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = "UPDATE Books SET"
        query_args = []
        if title:
            query += " title=%s,"
            query_args.append(title)
        if genre:
            query += " genre=%s,"
            query_args.append(genre)
        if publisher:
            query += " publisher=%s,"
            query_args.append(publisher)
        if rating is not None:
            query += " rating=%s,"
            query_args.append(rating)
        if copies_sold is not None:
            query += " copies_sold=%s,"
            query_args.append(copies_sold)
        if discount is not None:
            query += " discount=%s,"
            query_args.append(discount)

        query = query.rstrip(',')
        query += " WHERE id=%s"
        query_args.append(book_id)

        cursor.execute(query, query_args)
        conn.commit()

        return jsonify({'message': 'Book updated successfully'}), 200

    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)}), 500

    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
