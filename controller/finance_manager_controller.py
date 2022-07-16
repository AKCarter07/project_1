from flask import Blueprint, request
from service.reimb_service import ReimbService
from model.reimbursement import Reimbursement
from exception.invalid_param import InvalidParamError

fmc = Blueprint('finance_manager_controller', __name__)
rs = ReimbService()

# As a finance manager, I want to be able to view and approve reimbursement requests

@fmc.route('/fm/<username>/reimbursements')
def get_all_reimbs_fm():
    cookie = request.cookies.get('login')
    json_entry = request.get_json()
    try:
        rs.get_all_reimbs(None, json_entry['filter_status'], json_entry['filter_type'], cookie['role'])
    except InvalidParamError as e:
        return {
                   'message': f"{e}"
               }, 400