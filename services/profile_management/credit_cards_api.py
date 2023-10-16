from flask import Flask, jsonify, request
import mysql.connector

app: Flask = Flask(__name__)

# Database configuration
db_config = {
    'host': 'HOST_8',
    'user': 'team_8',
    'password': 'PASSWORD_8',
    'database': 'team_8'
}

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


if __name__ == '__main__':
    app.run(debug=True)
