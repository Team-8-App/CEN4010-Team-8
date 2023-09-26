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


@app.route('/books', methods=['GET'])
def get_books():
    genre_filter = request.args.get('genre')
    sort_by = request.args.get('sort_by', 'title')  # default is by title

    # Check if the sort_by value is valid to prevent SQL injection
    valid_sort_columns = ["title", "genre", "copies_sold", "rating", "publisher", "discount"]
    if sort_by not in valid_sort_columns:
        return jsonify({'error': 'Invalid sort column'})

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM Books"
        query_args = []

        if genre_filter:
            query += " WHERE genre=%s"
            query_args.append(genre_filter)

        query += f" ORDER BY {sort_by}"

        cursor.execute(query, query_args)
        books = cursor.fetchall()

        return jsonify(books)

    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)})

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


if __name__ == '__main__':
    app.run(debug=True)

