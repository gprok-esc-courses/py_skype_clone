import mysql.connector


class DBConnection:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost', user='test', password='test', database='python_skype_clone'
        )
        # EXERCISE 1: Create the 'users' and 'messages' tables if they do not exist
        # also add (seed) with sample data (users)


# Columns: id (AI), username, password (hashed), last_seen (datetime), online (boolean)
class User:
    def create_table(self):
        pass

    def seed(self):
        pass


# Columns: id (AI), sender_id (FK User), receiver_id (FK User), message (longtext), send_date (datetime)
class Message:
    def create_table(self):
        pass