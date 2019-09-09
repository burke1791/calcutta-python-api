from flask import Flask
from user_controller import UserController

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)