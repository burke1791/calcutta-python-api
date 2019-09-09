from flask import Flask, request, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'python_test'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
app.config['MYSQL_DATABASE_PORT'] = 8889
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def insert_user(self):
        insert_statement = (
            'INSERT INTO users (username, email) '
            'VALUES (%s, %s)'
        )
        data = (self.username, self.email)
        cursor.execute(insert_statement, data)
        conn.commit();

    def serialize(self):
        return {
            'username': self.username,
            'email': self.email
        }

# endpoint to create new user
@app.route('/user', methods=['POST'])
def add_user():
    username = request.json['username']
    email = request.json['email']

    new_user = User(username, email)
    new_user.insert_user()

    return jsonify(new_user.serialize())

# endpoint to show all users
@app.route('/user', methods=['GET'])
def get_user():
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()
    if data is None:
        return 'No users in the database'
    else:
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)