from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
class book :
    def __init__(self,data_dict) :
        self.id = data_dict['id']
        self.username = data_dict['username']
        self.age = data_dict['age']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users
    @classmethod
    def create_user(cls, data):
        query = """
        INSERT INTO users (username, age)
        VALUES (%(username)s ,%(age)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)
        