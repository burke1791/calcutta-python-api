from flask import Flask, request, jsonify
from user import User
from app import app


class UserController:
    @app.route('/user', methods=['GET'])
    def get_users():
        return User.get_all_users()