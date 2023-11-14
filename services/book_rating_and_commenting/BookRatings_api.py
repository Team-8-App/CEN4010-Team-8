from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'ls-b2f10f0f8d1f46949bc16b2a5608934e887eb6b0.c1zf3hrzxwhy.us-east-2.rds.amazonaws.com',
    'user': 'team_8',
    'password': 'Ankit-Bonnie-082821!',
    'database': 'team_8',
    'raise_on_warnings': True
}


@app.route('/ratings', methods=['GET', 'POST'])
def ratings():
    conn = None
    cursor = None

    if request.method == 'GET':
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM Ratings"
            cursor.execute(query)
            result = cursor.fetchall()
            return jsonify(result)

        except mysql.connector.Error as err:
            return jsonify({'error': 'Database error', 'message': str(err)})

        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    elif request.method == 'POST':
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            data = request.json
            book_id, user_id, rating = data.get('book_id'), data.get('user_id'), data.get('rating')

            if not all([book_id, user_id, rating]):
                return jsonify({'error': 'Missing required fields'}), 400

            query = "INSERT INTO Ratings (book_id, user_id, rating) VALUES (%s, %s, %s)"
            params = (book_id, user_id, rating)

            cursor.execute(query, params)
            conn.commit()

            return jsonify({'message': 'Rating created successfully'}), 201

        except mysql.connector.Error as err:
            return jsonify({'error': 'Database error', 'message': str(err)})

        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()


@app.route('/comments', methods=['GET', 'POST'])
def comments():
    conn = None
    cursor = None

    if request.method == 'GET':
        # Handle GET request for comments
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor(dictionary=True)

            query = "SELECT * FROM Comments"
            cursor.execute(query)
            comments = cursor.fetchall()

            return jsonify(comments)

        except mysql.connector.Error as err:
            return jsonify({'error': 'Database error', 'message': str(err)})

        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    elif request.method == 'POST':
        # Handle POST request for comments
        data = request.json
        book_id, user_id, comment = data.get('book_id'), data.get('user_id'), data.get('comment')

        if not all([book_id, user_id, comment]):
            return jsonify({'error': 'Missing required fields'}), 400

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            query = "INSERT INTO Comments (book_id, user_id, comment) VALUES (%s, %s, %s)"
            cursor.execute(query, (book_id, user_id, comment))
            conn.commit()

            return jsonify({'message': 'Comment created successfully'}), 201

        except mysql.connector.Error as err:
            return jsonify({'error': 'Database error', 'message': str(err)})

        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()


@app.route('/books/<int:book_id>/comments', methods=['GET'])
def get_book_comments(book_id):
    conn = None
    cursor = None

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM Comments WHERE book_id = %s"
        cursor.execute(query, (book_id,))
        comments = cursor.fetchall()

        return jsonify(comments)

    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)})

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

        query = "SELECT AVG(rating) AS average_rating FROM Ratings WHERE book_id = %s"
        cursor.execute(query, (book_id,))
        avg_rating = cursor.fetchone()

        return jsonify({'average_rating': avg_rating['average_rating']})

    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)})

    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    app.run(debug=True)
