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

# ---------------------------------------------
# User Profiles
# ---------------------------------------------
@app.route('/createUser', methods=['POST'])
def create_user():
    data = request.get_json()
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = "INSERT INTO UserProfiles (username, password, name, email, address) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (data['username'], data['password'], data.get('name', None), data.get('email', None), data.get('address', None)))
        conn.commit()
        return jsonify({'message': 'User created successfully!'})
    except mysql.connector.Error as err:
        return jsonify({'message': 'Failed to create user: {}'.format(err)})
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# ... [similar endpoints for updating user, creating credit card, etc.]

# ---------------------------------------------
# Book Details
# ---------------------------------------------
@app.route('/createBook', methods=['POST'])
def create_book():
    data = request.get_json()
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = "INSERT INTO BookDetails (isbn, book_name, description) VALUES (%s, %s, %s)"
        cursor.execute(query, (data['isbn'], data['book_name'], data['description']))
        conn.commit()
        return jsonify({'message': 'Book added successfully!'})
    except mysql.connector.Error as err:
        return jsonify({'message': 'Failed to add book: {}'.format(err)})
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# ... [similar endpoints for other book-related operations]

# ---------------------------------------------
# Shopping Cart
# ---------------------------------------------
@app.route('/addToCart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = "INSERT INTO ShoppingCart (user_id, book_isbn, quantity) VALUES (%s, %s, %s)"
        cursor.execute(query, (data['user_id'], data['book_isbn'], data['quantity']))
        conn.commit()
        return jsonify({'message': 'Book added to cart successfully!'})
    except mysql.connector.Error as err:
        return jsonify({'message': 'Failed to add book to cart: {}'.format(err)})
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# ... [similar endpoints for other shopping cart operations]

if __name__ == '__main__':
    app.run(debug=True)
