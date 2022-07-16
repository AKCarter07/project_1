from dao.reimb_dao import ReimbDao
from model.reimbursement import Reimbursement

# Read
#     Employee: where reimb_author = employee_id
#     FM: where reimb_author = *

class ReimbService():
    def __init__(self):
        self.rd = ReimbDao()

# Create
    def create_reimb(self, reimb_object):
        return self.rd.create_reimb(reimb_object)


# Read - as employee, as finance manager

    def get_reimb(self, reimb_id):
        return self.rd.get_reimb()

    def get_all_reimbs(self, user_id, filter_status, filter_type, role):
        return self.rd.get_reimbs(user_id, filter_status, filter_type)


# Update - as employee? as finance manager
    def update_reimb_status(self, reimb_obj):
        return self.rd.update_reimb_status(reimb_obj)

# Delete
    def delete_reimb(self, reimb_id):
        return self.rd.delete_reimb(reimb_id)