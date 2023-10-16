from flask import Flask, jsonify, request
import mysql.connector
app = Flask(__name__)

#Database Configuration
db_config = {
    'host': 'HOST_8',
    'user': 'team_8',
    'password': 'PASSWORD_8',
    'database': 'team_8'
}

#GET request to retrieve all book ratings
@app.route('/ratings', methods=['GET'])
def get_ratings():
    query = 'SELECT*FROM BookRatings'
    cursor.execute(query)
    ratings = cursor.fetchall()
    return jsonify(ratings)

if __name__ == '__main__':
    app.run(debug=True)