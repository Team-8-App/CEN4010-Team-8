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

@app.route('/books', methods=['GET'])
def get_books():
    genre_filter = request.args.get('genre')
    sort_by = request.args.get('sort_by', 'title')
    publisher_discount = request.args.get('publisher_discount')
    min_rating = request.args.get('min_rating', type=float)
    top_sellers = request.args.get('top_sellers', type=int)

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


if __name__ == '__main__':
    app.run(debug=True)
