from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'HOST_8',
    'user': 'team_8',
    'password': 'PASSWORD_8',
    'database': 'team_8'
    'raise_on_warnings': True
}


@app.route('/ratings', methods=['POST'])
def create_rating():
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
        if conn.is_connected():
            cursor.close()
            conn.close()


@app.route('/ratings/comment', methods=['POST'])
def create_comment():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        book_id = request.json['book_id']
        user_id = request.json['user_id']
        comment = request.json['comment']
        
        insert_query = ("INSERT INTO BookRatings (book_id, user_id, comment) "
                        "VALUES (%s, %s, %s)")
        cursor.execute(insert_query, (book_id, user_id, comment))
        conn.commit()

        return jsonify({'message': 'Comment created successfully'}), 201
    
    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)}), 500
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


@app.route('/books/<int:book_id>/comments', methods=['GET'])
def get_comments(book_id):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM BookRatings WHERE book_id = %s", (book_id,))
        comments = cursor.fetchall()
        return jsonify(comments)
    
    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)}), 500
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


@app.route('/books/<int:book_id>/average_rating', methods=['GET'])
def get_average_rating(book_id):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT AVG(rating) AS avg_rating FROM BookRatings WHERE book_id = %s", (book_id,))
        avg_rating = cursor.fetchone()

        return jsonify({'average_rating': avg_rating['avg_rating']})
    
    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)}), 500
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


if __name__ == '__main__':
    app.run(debug=True)
