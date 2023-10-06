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


def validate_user_owns_wishlist(user_id, wishlist_id, cursor):
    cursor.execute("SELECT user_id FROM WishLists WHERE wishlist_id = %s", (wishlist_id,))
    result = cursor.fetchone()
    return result and result['user_id'] == user_id


# Retrieve all wishlists for a user
@app.route('/user/<int:user_id>/wishlists', methods=['GET'])
def get_all_wishlists(user_id):
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM WishLists WHERE user_id = %s", (user_id,))
        wishlists = cursor.fetchall()
        return jsonify(wishlists)
    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)})
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()


# Create a new wishlist for a user
@app.route('/user/<int:user_id>/wishlist', methods=['POST'])
def create_wishlist(user_id):
    conn = None
    cursor = None
    wishlist_name = request.json['wishlist_name']
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO WishLists (user_id, wishlist_name) VALUES (%s, %s)", (user_id, wishlist_name))
        conn.commit()
        return jsonify({"message": "Wishlist created successfully!"})
    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)})
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()


# Add a book to a specific wishlist
@app.route('/user/<int:user_id>/wishlist/<int:wishlist_id>/book/<int:book_id>', methods=['POST'])
def add_book_to_wishlist(user_id, wishlist_id, book_id):
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        if not validate_user_owns_wishlist(user_id, wishlist_id, cursor):
            return jsonify({"error": "The wishlist does not belong to the provided user."}), 403

        cursor.execute("INSERT INTO WishListItems (wishlist_id, book_id) VALUES (%s, %s)", (wishlist_id, book_id))
        conn.commit()
        return jsonify({"message": "Book added to wishlist successfully!"})
    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)})
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()


# Remove a book from a specific wishlist
@app.route('/user/<int:user_id>/wishlist/<int:wishlist_id>/book/<int:book_id>', methods=['DELETE'])
def remove_book_from_wishlist(user_id, wishlist_id, book_id):
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        if not validate_user_owns_wishlist(user_id, wishlist_id, cursor):
            return jsonify({"error": "The wishlist does not belong to the provided user."}), 403

        cursor.execute("DELETE FROM WishListItems WHERE wishlist_id = %s AND book_id = %s", (wishlist_id, book_id))
        conn.commit()
        return jsonify({"message": "Book removed from wishlist successfully!"})
    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)})
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()


# Retrieve all books in a specific wishlist
@app.route('/user/<int:user_id>/wishlist/<int:wishlist_id>/books', methods=['GET'])
def get_books_in_wishlist(user_id, wishlist_id):
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        if not validate_user_owns_wishlist(user_id, wishlist_id, cursor):
            return jsonify({"error": "The wishlist does not belong to the provided user."}), 403

        cursor.execute("""
            SELECT b.* 
            FROM Books b
            JOIN WishListItems wli ON b.book_id = wli.book_id
            WHERE wli.wishlist_id = %s;
        """, (wishlist_id,))
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
