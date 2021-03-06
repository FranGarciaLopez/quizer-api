from lib.response_parser import Response_Parser
from lib.db import Db

class UserQuestions:
    def __init__(self, conn):
        self.conn = conn

    def post(self, user_id, question_id):
        sql_statement = "INSERT INTO user_questions (user_id, question_id) VALUES ('{0}','{1}')".format(user_id, question_id)

        response = self.conn.engine.execute(sql_statement)
        return Response_Parser.post(response)
        
    def get_all(self, user_id):
        sql_statement = "SELECT * FROM user_questions where user_id = '{0}'".format(user_id)

        response = self.conn.engine.execute(sql_statement)
        return Response_Parser.get(response)
    
    def get_one(self, user_id, question_id):
        sql_statement = "SELECT * FROM user_questions WHERE user_id = '{0}' and question_id = '{1}'".format(user_id, question_id)

        response = self.conn.engine.execute(sql_statement)
        return Response_Parser.get(response)

    def put(self, user_id, question_id):
        sql_statement = "UPDATE user_questions SET user_id = '{0}', question_id = '{1}'".format(user_id, question_id)

        response = self.conn.engine.execute(sql_statement)
        return Response_Parser.put(response)

    def delete_all(self, table_name, id_name, id_value):
        Db.delete_all_subelement(self, table_name, id_name, id_value)

    def delete(self, user_id, question_id):
        sql_statement = "DELETE FROM user_questions WHERE user_id = '{0}' and question_id = '{1}'".format(user_id, question_id)

        response = self.conn.engine.execute(sql_statement)
        return Response_Parser.delete(response)
    
