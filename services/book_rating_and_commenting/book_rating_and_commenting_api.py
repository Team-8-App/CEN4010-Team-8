from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL configuration
mysql_host = 'HOST_8',
mysql_user = 'team_8',
mysql_password = 'PASSWORD_8',
mysql_db = 'team_8'

# Connect to MySQL
db = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_db
)

# Create a cursor object to interact with the database
cursor = db.cursor(dictionary=True)

# GET request to retrieve all book ratings
@app.route('/ratings', methods=['GET'])
def get_ratings():
    query = 'SELECT * FROM BookRatings'
    cursor.execute(query)
    ratings = cursor.fetchall()
    return jsonify(ratings)

if __name__ == '__main__':
    app.run(debug=True)
