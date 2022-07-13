from model.reimbursement import Reimbursement
import psycopg


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
    def get_reimb_by_user(self, user_id):
        reimbs = []
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="pass") as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM ers_reimbursement WHERE reimb_author = '{user_id}';")
                for line in cur:
                    reimb = Reimbursement(line[1], line[2], line[5], line[6], line[7], line[8])
                    reimb.set_id(line[0])
                    reimb.set_status(line[4])
                    reimb.set_resolved(line[3])
                    reimb.set_resolver(line[9])
                    reimbs.append(reimb)
            return reimbs

    def get_all_reimbs(self):
        reimbs = []
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="pass") as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM ers_reimbursement;")
                for line in cur:
                    reimb = Reimbursement(line[1], line[2], line[5], line[6], line[7], line[8])
                    reimb.set_id(line[0])
                    reimb.set_status(line[4])
                    reimb.set_resolved(line[3])
                    reimb.set_resolver(line[9])
                    reimbs.append(reimb)
            return reimbs



# Update


# Delete
