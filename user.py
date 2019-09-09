from flask import jsonify
from flaskext.mysql import MySQL
from app import app

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

    def get_all_users(self):
        select_statement = 'SELECT * FROM users'
        cursor.execute(select_statement)
        data = cursor.fetchall()
        return jsonify(data)

    def serialize(self):
        return {
            'username': self.username,
            'email': self.email
        }