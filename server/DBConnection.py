import mysql.connector


class DBConnection:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost', user='test', password='test', database='python_skype_clone'
        )
        User.create_table(self.connection)
        User.seed(self.connection)
        Message.create_table(self.connection)


# Columns: id (AI), username, password (hashed), last_seen (datetime), online (boolean)
class User:
    @staticmethod
    def create_table(conn):
        create_users_table_query = """
                    CREATE TABLE IF NOT EXISTS users (
                      id INT AUTO_INCREMENT PRIMARY KEY,
                      username VARCHAR(255) NOT NULL,
                      password VARCHAR(255) NOT NULL,
                      last_seen DATETIME,
                      online TINYINT DEFAULT 0
                    )
                """
        cursor = conn.cursor()
        cursor.execute(create_users_table_query)

    @staticmethod
    def seed(conn):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        cursor.fetchall()
        rows = cursor.rowcount
        if rows == 0:
            insert_seed_data_query = """
                   INSERT INTO users (username, password, last_seen)
                   VALUES ('john', SHA1('test'), NOW()), 
                   ('mary', SHA1('test'), NOW()),
                   ('mike', SHA1('test'), NOW())
               """
            cursor.execute(insert_seed_data_query)


# Columns: id (AI), sender_id (FK User), receiver_id (FK User), message (longtext), send_date (datetime)
class Message:
    @staticmethod
    def create_table(conn):
        create_messages_table_query = """
                    CREATE TABLE IF NOT EXISTS messages (
                      id int AUTO_INCREMENT PRIMARY KEY,
                      sender_id INT NOT NULL,
                      receiver_id INT NOT NULL,
                      message longtext NOT NULL,
                      send_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                      FOREIGN KEY (receiver_id) REFERENCES users (id),
                      FOREIGN KEY (sender_id) REFERENCES users (id)
                    );
                """
        cursor = conn.cursor()
        cursor.execute(create_messages_table_query)