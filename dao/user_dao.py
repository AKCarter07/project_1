from model.user import User
import psycopg

class UserDao:
    def __init__(self):
        pass


# Create
    def create_user(self, user_object):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="pass") as conn:
            with conn.cursor() as cur:
                cur.execute(f"INSERT INTO ers_users (username, password, first_name, last_name, email, role) "
                            f"VALUES ('{user_object.username}', '{user_object.password}', '{user_object.fname}', "
                            f"'{user_object.lname}', '{user_object.email}', '{user_object.role}');")
                conn.commit()
                return f"User {user_object.username} has been added to the system."

# Read
    def get_user(self, username):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="pass") as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM ers_users WHERE username = '{username}';")
                for line in cur:
                    user = User(line[1], line[2], line[3], line[4], line[5], line[6])
                    user.set_user_id(line[0])
                    return user
# Update
# Delete

