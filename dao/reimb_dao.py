from model.reimbursement import Reimbursement
import psycopg
import datetime


class ReimbDao:
    def __init__(self):
        pass

#(self, amount, submitted, type, descrip, receipt, author)
# Create
    def create_reimb(self, reimb_obj):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="pass") as conn:
            with conn.cursor() as cur:
                cur.execute(f"INSERT INTO ers_reimbursement (reimb_amount, submitted, reimb_type, description, "
                            f"receipt, reimb_author, status) VALUES ('{reimb_obj.amount}', '{reimb_obj.submitted}', "
                            f"'{reimb_obj.type}', '{reimb_obj.descrip}', '{reimb_obj.receipt}', '{reimb_obj.author}', "
                            f"'{reimb_obj.status}');")
                conn.commit()
        return "this blows"

# Read
    def get_reimb(self, reimb_id):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="pass") as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM ers_reimbursement WHERE reimb_id = '{reimb_id}';")
                for line in cur:
                    reimb = Reimbursement(line[1], line[2], line[5], line[6], line[7], line[8])
                    reimb.set_id(line[0])
                    reimb.set_status(line[4])
                    reimb.set_resolved(line[3])
                    reimb.set_resolver(line[9])
                    return reimb

    def get_reimbs(self, user_id, filter_status, filter_type):
        reimbs = []
        call = "SELECT * FROM ers_reimbursement"
        if not user_id is None or not filter_status is None or not filter_type is None:
            call = call + f" WHERE "
            if not user_id is None:
                call = call + f"reimb_author = '{user_id}'"
                if not filter_status is None or not filter_type is None:
                    call = call + " AND "
            if not filter_status is None:
                call = call + f"status = '{filter_status}'"
                if not filter_type is None:
                    call = call + " AND "
            if not filter_type is None:
                call = call + f"reimb_type = '{filter_type}'"
            call = call + ";"
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="pass") as conn:
            with conn.cursor() as cur:
                cur.execute(call)
                for line in cur:
                    reimb = Reimbursement(line[1], line[2], line[5], line[6], line[7], line[8])
                    reimb.set_id(line[0])
                    reimb.set_status(line[4])
                    reimb.set_resolved(line[3])
                    reimb.set_resolver(line[9])
                    reimbs.append(reimb)
            return reimbs

  
# Update
    def update_reimb(self, reimb_obj):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="pass") as conn:
            with conn.cursor() as cur:
                cur.execute(f"UPDATE ers_reimbursement SET status = '{reimb_obj.status}', resolved = "
                            f"'{datetime.datetime.now()}', reimb_resolver = '{reimb_obj.resolver}' WHERE reimb_id = "
                            f"'{reimb_obj.reimb_id}';")
                conn.commit()
                return f"Reimbursement request {reimb_obj.reimb_id} has been {reimb_obj.status}."



# Delete
