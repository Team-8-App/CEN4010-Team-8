from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'ls-b2f10f0f8d1f46949bc16b2a5608934e887eb6b0.c1zf3hrzxwhy.us-east-2.rds.amazonaws.com',
    'user': 'team_8',
    'password': 'Ankit-Bonnie-082821!',
    'database': 'team_8'
}

@app.route('/books', methods=['GET', 'POST'])
def get_books():
    genre_filter = request.args.get('genre')
    sort_by = request.args.get('sort_by', 'title')
    publisher_discount = request.args.get('publisher_discount')
    min_rating = request.args.get('min_rating', type=float)
    top_sellers = request.args.get('top_sellers', type=int)

    if request.method == 'GET':
        valid_sort_columns = ["title", "genre", "copies_sold", "rating", "publisher", "discount"]
        if sort_by not in valid_sort_columns:
            return jsonify({'error': 'Invalid sort column'})

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
            return jsonify({'error': 'Database error', 'message': str(err)})

        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    elif request.method == 'POST':
        conn = None
        cursor = None

        try:
            user_data = request.json

            title = user_data.get('title', None)
            genre = user_data.get('genre', None)
            copies_sold = user_data.get('copies_sold', None)
            publisher = user_data.get('publisher', None)
            discount = user_data.get('discount', None)
            book_id = user_data.get('book_id', None)

            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Insert the user into the database
            query = "INSERT INTO Books (book_id, title, genre, copies_sold, publisher, discount) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (book_id, title, genre, copies_sold, publisher, discount))

            conn.commit()
            return jsonify({'message': 'User created successfully'})

        except mysql.connector.Error as err:
            return jsonify({'error': 'Database error', 'message': str(err)})

        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()


if __name__ == '__main__':
    app.run(debug=True)
