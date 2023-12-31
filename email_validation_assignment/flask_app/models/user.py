from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = "user_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def valid_user(cls, user):
        is_valid = True

        if len(user['first_name']) <= 0:
            is_valid = False
            flash("First Name is required.")
        if len(user['last_name']) <= 0:
            is_valid = False
            flash("Last Name is required.")
        if len(user['email']) <= 0:
            is_valid = False
            flash("Email is required.")
        if len(user['email']) > 0 and not EMAIL_REGEX.match(user['email']):
            is_valid = False
            flash("invalid email format.")
        return is_valid

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        return connectToMySQL(cls.db).query_db(query)

    @classmethod
    def save_db(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES(%(first_name)s, %(last_name)s, %(email)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)