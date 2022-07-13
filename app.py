from dao.reimb_dao import ReimbDao
from model.reimbursement import Reimbursement
import datetime


#(self, amount, submitted, type, descrip, receipt, author)
rd = ReimbDao()
now = datetime.datetime.now()
re = Reimbursement(12.50, now, "other", "tololol", "idgaf", 4)

# print(rd.create_reimb(re))


# r7 = rd.get_reimb(7)
# r4 = rd.get_reimb(4)
#
# r7.set_status('approved')
# r4.set_status('denied')
# r7.set_resolver(1)
# r4.set_resolver(1)
# rd.update_reimb(r7)
# rd.update_reimb(r4)

res = rd.get_reimbs(3, None, None)
for reimb in res:
    print(reimb.to_dict())


