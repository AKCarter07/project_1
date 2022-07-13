from dao.reimb_dao import ReimbDao
from model.reimbursement import Reimbursement
import datetime


#(self, amount, submitted, type, descrip, receipt, author)
rd = ReimbDao()
now = datetime.datetime.now()
re = Reimbursement(12.50, now, "travel", "tololol", "idgaf", 2)

# print(rd.create_reimb(re))
res = rd.get_reimb_by_user(4)
for reimb in res:
    print(reimb.to_dict())

