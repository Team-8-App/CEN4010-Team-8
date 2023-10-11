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

@app.route('/book_detail', methods=['GET'])
def get_user_profile():
    conn = None
    cursor = None
    isbn_filter = request.args.get('isbn')
    author_filter = request.args.get('author_id')

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM BookDetails"
        query_args = []

        if isbn_filter:
            query += " WHERE isbn=%s"
            query_args.append(isbn_filter)

        elif author_filter:
            query += " WHERE author_id=%s"
            query_args.append(author_filter)

        cursor.execute(query, query_args)
        user_profile = cursor.fetchall()

        return jsonify(user_profile)

    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)})

    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()


@app.route('/books', methods=['POST'])
def create_book():
    conn = None
    cursor = None
    data = request.get_json()
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        insert_query = """INSERT INTO BookDetails(isbn, book_name, description, price, author_id, genre, publisher, year_published, copies_sold)
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(insert_query,
                       (data['isbn'], data['book_name'], data['description'], data['price'], data['author_id'],
                        data['genre'], data['publisher'], data['year_published'], data['copies_sold']))
        conn.commit()
        return jsonify({'status': 'Book created'}), 201

    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)})

    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()


@app.route('/authors/<int:author_id>/books', methods=['GET'])
def get_books_by_author(author_id):
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        select_query = "SELECT * FROM BookDetails WHERE author_id = %s"
        cursor.execute(select_query, (author_id,))
        books = cursor.fetchall()

        return jsonify(books), 200

    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)})

    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    app.run(debug=True)

