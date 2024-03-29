from lib.response_parser import Response_Parser
from .user_tests import UserTests
from .user_paths import UserPaths
from .user_questions import UserQuestions
from .user_resources import UserResources

class Users:
    def __init__(self, conn):
        self.conn = conn

    def post(self, data):
        name = data["name"]
        surname = data["surname"]
        nickname = data["nickname"]
        lang = data["lang"]
        email = data["email"]
        telegram_id = data["telegram_id"]
        password = data["password"]

        sql_statement = "INSERT INTO users (name, surname, nickname, lang, email, telegram_id, password) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}')"
        sql_statement = sql_statement.format(name, surname, nickname, lang, email, telegram_id, password)

        response = self.conn.engine.execute(sql_statement)
        return Response_Parser.post(response)
        
    def get_all(self):
        sql_statement = "SELECT * FROM users ORDER BY id ASC"
        response = self.conn.engine.execute(sql_statement)
        return Response_Parser.get(response)
    
    def get_one(self, user_id):
        sql_statement = "SELECT * FROM users WHERE id = '{0}'".format(user_id)

        response = self.conn.engine.execute(sql_statement)
        return Response_Parser.get(response)

    def put(self, user_id, data):
        name = data["name"]
        surname = data["surname"]
        nickname = data["nickname"]
        lang = data["lang"]
        email = data["email"]
        telegram_id = data["telegram_id"]
        password = data["password"]
        sql_statement = "UPDATE users SET name = '{0}', surname = '{1}', nickname = '{2}', lang = '{3}', email = '{4}', telegram_id = '{5}', password = '{6}' WHERE id = '{7}'"
        sql_statement = sql_statement.format(name, surname, nickname, lang, email, telegram_id, password, user_id)

        response = self.conn.engine.execute(sql_statement)
        return Response_Parser.put(response)
    
    def delete(self, user_id):
        
        UserPaths.delete_all(self, "user_paths", "user_id", user_id)
        UserTests.delete_all(self, "user_tests", "user_id", user_id)
        UserQuestions.delete_all(self, "user_questions", "user_id", user_id)
        UserResources.delete_all(self, "user_resources", "user_id", user_id)
        
        sql_statement = "DELETE FROM users WHERE id = '{0}'".format(user_id)

        response = self.conn.engine.execute(sql_statement)
        return Response_Parser.delete(response)
    
