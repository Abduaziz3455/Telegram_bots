import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            PRIMARY KEY (id)
            );
        """
        sql1 = """
        CREATE TABLE IF NOT EXISTS Groups (
            id int NOT NULL,
            g_name varchar(255) NOT NULL,
            ball int DEFAULT 0,
            PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)
        self.execute(sql1, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([f"{item} = ?" for item in parameters])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, type: int):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"
        sql = """
        INSERT INTO Users(id, Name) VALUES(?, ?)
        """
        sql1 = """
        INSERT INTO Groups(id, g_name) VALUES(?, ?)
        """

        if type == 1:
            self.execute(sql, parameters=(id, name), commit=True)
        else:
            self.execute(sql1, parameters=(id, name), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_all_group_users(self):
        sql = """
        SELECT * FROM Groups
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def select_group_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Groups WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_group_users(self):
        return self.execute("SELECT COUNT(*) FROM Groups;", fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def plus(self, nom: int):
        sql = "UPDATE Groups SET ball = ball + 1 WHERE g_name = ?"
        sql1 = "SELECT ball FROM Groups WHERE g_name = ?"
        self.execute(sql, parameters=(nom,), commit=True)
        return self.execute(sql1, parameters=(nom,), fetchone=True)

    # def update_user_email(self, email, id):
    #     # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"
    #
    #     sql = f"""
    #     UPDATE Users SET email=? WHERE id=?
    #     """
    #     return self.execute(sql, parameters=(email, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Groups WHERE TRUE", commit=True)

    def default_state(self):
        self.execute("UPDATE Groups SET ball = 0", commit=True)

    def summary(self):
        return self.execute("SELECT g_name, ball FROM Groups", fetchall=True)



def logger(statement):
    print(f"""
_____________________________________________________
Executing: 
{statement}
_____________________________________________________
""")
