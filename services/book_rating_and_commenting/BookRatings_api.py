from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'HOST_8',
    'user': 'team_8',
    'password': 'PASSWORD_8',
    'database': 'team_8',
    'raise_on_warnings': True  # Added a comma before this line
}


@app.route('/ratings', methods=['POST'])
def create_rating():
    conn = None
    cursor = None

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        book_id = request.json['book_id']
        user_id = request.json['user_id']
        rating = request.json['rating']

        insert_query = ("INSERT INTO BookRatings (book_id, user_id, rating) "
                        "VALUES (%s, %s, %s)")
        cursor.execute(insert_query, (book_id, user_id, rating))
        conn.commit()

        return jsonify({'message': 'Rating created successfully'}), 201

    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)}), 500

    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()


@app.route('/ratings/comment', methods=['POST'])
def create_comment():
    conn = None
    cursor = None

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        book_id = request.json['book_id']
        user_id = request.json['user_id']
        comment = request.json['comment']

        insert_query = ("INSERT INTO BookRatings (book_id, user_id, comment, rating) "
                        "VALUES (%s, %s, %s, %s)")
        cursor.execute(insert_query, (book_id, user_id, comment))
        conn.commit()

        return jsonify({'message': 'Comment created successfully'}), 201

    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)}), 500

    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()


@app.route('/books/<int:book_id>/comments', methods=['GET'])
def get_comments(book_id):
    conn = None
    cursor = None

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM BookRatings WHERE book_id = %s", (book_id,))
        comments = cursor.fetchall()

        return jsonify(comments)

    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)}), 500

    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()


@app.route('/books/<int:book_id>/average_rating', methods=['GET'])
def get_average_rating(book_id):
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT AVG(rating) AS rating FROM BookRatings WHERE book_id = %s", (book_id,))
        avg_rating = cursor.fetchone()

        # Ensure avg_rating is a dict before proceeding
        if not isinstance(avg_rating, dict):
            raise TypeError("avg_rating is not a dictionary.")

        return jsonify({'average_rating': avg_rating['rating']})

    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)}), 500
    except TypeError as te:
        return jsonify({'error': 'Type error', 'message': str(te)}), 500
    finally:
        if conn and conn.is_connected():
            if cursor:
                cursor.close()
            conn.close()


if __name__ == '__main__':
    app.run(debug=True)

