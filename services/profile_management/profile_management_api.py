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
headers = {
    'Content-Type': 'application/json'
}

@app.route('/user-profile', methods=['GET', 'POST'])
def user_profile():
    conn = None
    cursor = None

    if request.method == 'GET':
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
            user_profiles = cursor.fetchall()

            return jsonify(user_profiles)

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
            # Get user data from the request
            user_data = request.json  # Assuming the data is sent as JSON in the request body

            # Extract required fields
            username = user_data.get('username')
            password = user_data.get('password')

            # Optional fields
            name = user_data.get('name', None)
            email_address = user_data.get('email_address', None)
            home_address = user_data.get('home_address', None)
            user_id = user_data.get('user_id', None)

            if not (username and password):
                return jsonify({'error': 'Username and password are required fields'})

            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Insert the user into the database
            query = "INSERT INTO UserProfile (user_id, username, password, name, email_address, home_address) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (user_id, username, password, name, email_address, home_address))

            conn.commit()
            return jsonify({'message': 'User created successfully'})

        except mysql.connector.Error as err:
            return jsonify({'error': 'Database error', 'message': str(err)})

        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()


@app.route('/user-profile/<int:user_id>', methods=['PUT', 'PATCH'])
def update_profile(user_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:
        # Extract user data from the request
        user_data = request.json  # Assuming the data is sent as JSON in the request body

        # Check if the user with the given user_id exists
        cursor.execute("SELECT * FROM UserProfile WHERE user_id = %s", (user_id,))
        existing_user = cursor.fetchone()
        if not existing_user:
            return jsonify({'error': f'User with ID {user_id} not found'})

        # Extract the fields to be updated (except email)
        updated_fields = {}
        for field in ['username', 'home_address', 'password', 'name']:
            if field in user_data and field != 'email':
                updated_fields[field] = user_data[field]

        if not updated_fields:
            return jsonify({'error': 'No valid fields to update provided'})

        # Construct the SQL query
        set_clause = ', '.join([f"{field}=%s" for field in updated_fields])
        query = f"UPDATE UserProfile SET {set_clause} WHERE user_id = %s"
        cursor.execute(query, tuple(updated_fields.values()) + (user_id,))

        conn.commit()
        return jsonify({'message': f'User with ID {user_id} updated successfully'})

    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)})

    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()
            
@app.route('/user-profile/<int:user_id>', methods=['DELETE'])
def delete_profile(user_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:
        # Check if the user with the given user_id exists
        cursor.execute("SELECT * FROM UserProfile WHERE user_id = %s", (user_id,))
        existing_user = cursor.fetchone()
        if not existing_user:
            return jsonify({'error': f'User with ID {user_id} not found'})

        # Delete the user profile with the specified user_id
        cursor.execute("DELETE FROM UserProfile WHERE user_id = %s", (user_id,))

        conn.commit()
        return jsonify({'message': f'User with ID {user_id} deleted successfully'})

    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)})

    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

@app.route('/credit-card', methods=['GET', 'POST'])
def credit_card():
    conn = None
    cursor = None
    user_id = request.args.get('user_id')

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # Retrieving credit cards by user_id
        if request.method == 'GET':
            if user_id:
                select_query = "SELECT * FROM CreditCards WHERE user_id=%s"
                cursor.execute(select_query, (user_id,))
                cards = cursor.fetchall()
                return jsonify(cards)
            else:
                return jsonify({"error": "User ID is required"}), 400

        # Adding a new credit card
        elif request.method == 'POST':
            card_data = request.get_json()
            insert_query = """INSERT INTO CreditCards (user_id, card_number, expiry_date, cvv, card_holder_name) 
                              VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(insert_query, (
                card_data['user_id'],
                card_data['card_number'],
                card_data['expiry_date'],
                card_data['cvv'],
                card_data['card_holder_name']
            ))
            conn.commit()
            return jsonify({"message": "Card added"}), 201

    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)}), 500

    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()
@app.route('/credit-card/<int:user_id>', methods=['DELETE'])
def delete_credit_card(user_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM CreditCards WHERE user_id = %s", (user_id,))
        existing_user = cursor.fetchone()
        if not existing_user:
            return jsonify({'error': f'User with ID {user_id} not found'})

        cursor.execute("DELETE FROM CreditCards WHERE user_id = %s", (user_id,))

        conn.commit()
        return jsonify({'message': f'CreditCards with ID {user_id} deleted successfully'})

    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)})

    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
