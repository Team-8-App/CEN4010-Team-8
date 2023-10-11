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

@app.route('/shopping-cart', methods=['GET'])
def get_user_profile():
    conn = None
    cursor = None
    user_id = request.args.get('user_id')

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # Define the base query
        select_all = """
            SELECT * from ShoppingCart
        """

        # Define the base query
        base_query = """
            SELECT b.book_id, b.title, b.publisher, b.discount, ci.quantity, (ci.quantity * ci.price) AS subtotal
            FROM CartItem ci
            JOIN Books b ON ci.book_id = b.book_id
        """

        if user_id:
            # If user_id is provided, add a WHERE clause to filter by user_id
            query = f"{base_query} WHERE ci.cart_id IN (SELECT cart_id FROM ShoppingCart WHERE user_id = %s)"
            cursor.execute(query, (user_id,))
        else:
            # If user_id is not provided, retrieve all items in the cart
            cursor.execute(select_all)

        books_in_cart = cursor.fetchall()

        if books_in_cart:
            return jsonify(books_in_cart)
        else:
            return jsonify({'error': 'Cart is empty'})

    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)})

    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    app.run(debug=True)
