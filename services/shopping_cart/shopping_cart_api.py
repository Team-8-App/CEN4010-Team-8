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


@app.route('/shopping-cart', methods=['GET', 'POST'])
def shopping_cart():
    conn = None
    cursor = None
    user_id = request.args.get('user_id')

    if request.method == 'GET':
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor(dictionary=True)

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
                return jsonify({'error': 'User ID is required'})

            books_in_cart = cursor.fetchall()

            if books_in_cart:
                subtotal = sum(float(item['subtotal']) for item in books_in_cart)
                return jsonify({'books': books_in_cart, 'subtotal': subtotal})
            else:
                return jsonify({'error': 'Cart is empty'})

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

            # Get data from the request
            data = request.json

            # Extract required fields
            user_id = data.get('user_id')
            book_id = data.get('book_id')
            quantity = data.get('quantity', 1)
            price = data.get('price')

            if not user_id or not book_id or price is None:
                return jsonify({'error': 'User ID, Book ID, and Price are required fields'})

            # Check if the book already exists in the cart
            cursor.execute(
                "SELECT * FROM CartItem WHERE cart_id IN (SELECT cart_id FROM ShoppingCart WHERE user_id = %s) AND book_id = %s",
                (user_id, book_id),
            )
            existing_book = cursor.fetchone()

            if existing_book:
                # Update the quantity of the existing book
                new_quantity = int(existing_book['quantity']) + int(quantity)
                cursor.execute(
                    "UPDATE CartItem SET quantity = %s WHERE item_id = %s",
                    (new_quantity, int(existing_book['item_id'])),
                )
            else:
                # Add the new book to the cart
                cursor.execute(
                    "INSERT INTO CartItem (cart_id, book_id, quantity, price) VALUES ((SELECT cart_id FROM ShoppingCart WHERE user_id = %s), %s, %s, %s)",
                    (user_id, book_id, quantity, price),
                )

            conn.commit()
            return jsonify({'message': 'Book added to cart successfully'})

        except mysql.connector.Error as err:
            return jsonify({'error': 'Database error', 'message': str(err)})

        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()


@app.route('/shopping-cart/<int:book_id>', methods=['DELETE'])
def delete_book_from_cart(book_id):
    conn = None
    cursor = None
    user_id = request.args.get('user_id')

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Check if the book exists in the user's cart
        cursor.execute(
            "SELECT * FROM CartItem WHERE cart_id IN (SELECT cart_id FROM ShoppingCart WHERE user_id = %s) AND book_id = %s",
            (user_id, book_id),
        )
        existing_book = cursor.fetchone()

        if not existing_book:
            return jsonify({'error': 'Book not found in cart'})

        # Delete the book from the cart
        cursor.execute(
            "DELETE FROM CartItem WHERE item_id = %s",
            (int(existing_book['item_id']),),
        )

        conn.commit()
        return jsonify({'message': 'Book deleted from cart successfully'})

    except mysql.connector.Error as err:
        return jsonify({'error': 'Database error', 'message': str(err)})

    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    app.run(debug=True)

