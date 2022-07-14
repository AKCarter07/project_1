from dao.reimb_dao import ReimbDao
from model.reimbursement import Reimbursement
import datetime
from dao.user_dao import UserDao


#(self, amount, submitted, type, descrip, receipt, author)
rd = ReimbDao()
now = datetime.datetime.now()
re = Reimbursement(12.50, now, "other", "tololol", "idgaf", 4)
ud = UserDao()

# print(rd.create_reimb(re))


# r7 = rd.get_reimb(7)
# r4 = rd.get_reimb(4)
#
# r7.set_status('approved')
# r4.set_status('denied')
# r7.set_resolver(1)
# r4.set_resolver(1)
# rd.update_reimb_status(r7)
# rd.update_reimb_status(r4)


# res = rd.get_reimbs(None, None, None)
# for reimb in res:
#     print(reimb.to_dict())

u2 = ud.get_user('paladin1')
print(u2.to_dict())


