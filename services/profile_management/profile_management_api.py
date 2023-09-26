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

@app.route('/user-profile', methods=['GET'])
def get_user_profile():    
    username_filter = request.args.get('username')
    sort_by = request.args.get('sort_by', 'username') 

    # Check if the sort_by value is valid to prevent SQL injection
    valid_sort_columns = ["username", "user_id"]
    if sort_by not in valid_sort_columns:
        return jsonify({'error': 'Invalid sort column'})

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM UserProfile"
        query_args = []

        if username_filter:
            query += " WHERE username=%s"
            query_args.append(username_filter)

        query += f" ORDER BY {sort_by}"

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

