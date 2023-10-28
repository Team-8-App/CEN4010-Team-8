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


@app.route('/book_detail', methods=['GET', 'POST'])
def get_book_details():
    conn = None
    cursor = None

    if request.method == 'GET':
        isbn_filter = request.args.get('isbn')
        sort_by = request.args.get('sort_by', 'isbn')
        author_filter = request.args.get('author_id')

        valid_sort_columns = ["isbn", "author_id"]

        if sort_by not in valid_sort_columns:
            return jsonify({'error': 'Invalid sort column'})

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor(dictionary=True)

            query = "SELECT * FROM BookDetails"
            query_args = []

            if isbn_filter:
                query += " WHERE isbn=%s"
                query_args.append(isbn_filter)

            if author_filter:
                query += " WHERE author_id=%s"
                query_args.append(author_filter)

            query += f" ORDER BY {sort_by}"

            cursor.execute(query, query_args)
            book_details = cursor.fetchall()

            return jsonify(book_details)

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

            isbn = user_data.get('isbn', None)
            book_name = user_data.get('book_name', None)
            description = user_data.get('description', None)
            price = user_data.get('price', None)
            author_id = user_data.get('author_id', None)
            genre = user_data.get('genre', None)
            publisher = user_data.get('publisher', None)
            year_published = user_data.get('year_published', None)
            copies_sold = user_data.get('copies_sold', None)

            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            query = "INSERT INTO BookDetails (isbn, book_name, description, price, author_id, genre, publisher, year_published, copies_sold) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (isbn, book_name, description, price, author_id, genre, publisher, year_published, copies_sold))

            conn.commit()
            return jsonify({'message': 'User created successfully'})

        except mysql.connector.Error as err:
            return jsonify({'error': 'Database error', 'message': str(err)})

        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

@app.route('/book_detail/<int:author_id>', methods=['PUT', 'PATCH'])
def update_book_detail(author_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:
        user_data = request.json

        cursor.execute("SELECT * FROM BookDetails WHERE author_id = %s", (author_id))
        existing_author = cursor.fetchone()
        if not existing_author:
            return jsonify({'error': f'Author with ID {author_id} not found'})

        updated_fields = {}
        for field in ['isbn', 'description', 'price', 'genre', 'publisher', 'year_published', 'copiSes_sold']:
            if field in user_data and field != 'book_name':
                updated_fields[field] = user_data[field]

            if not updated_fields:
                return jsonify({'error': 'No valid fields to update provided'})

        set_clause = ', '.join([f"{field}=%s" for field in updated_fields])
        query = f"UPDATE BookDetails SET {set_clause} WHERE author_id = %s"
        cursor.execute(query, tuple(updated_fields.values()) + (author_id))

        conn.commit()
        return jsonify({'message': f'Author with ID {author_id} updated successfully'})

    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)})

    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

@app.route('/book_detail/<int:author_id>', methods=['DELETE'])
def delete_profile(author_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM BookDetails WHERE author_id = %s", (author_id))

        conn.commit()
        return jsonify({'message': f'Author with ID {author_id} deleted successfully'})

    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)})

    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    app.run(debug=True)
