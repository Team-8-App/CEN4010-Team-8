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

@app.route('/book_detail', methods=['GET'])
def get_user_profile():    
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

        if author_filter:
            query += " WHERE author_id=%s"
            query_args.append(author_filter)

        cursor.execute(query, query_args)
        userProfile = cursor.fetchall()

        return jsonify(userProfile)

    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)})

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


if __name__ == '__main__':
    app.run(debug=True)

