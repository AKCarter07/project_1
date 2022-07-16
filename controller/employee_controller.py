from flask import Blueprint, request, session, redirect, url_for
from service.user_service import UserService
from service.reimb_service import ReimbService
from model.reimbursement import Reimbursement
from model.user import User
from exception.invalid_param import InvalidParamError
from controller.user_controller import uc

ec = Blueprint('employee_controller', __name__)
us = UserService()
rs = ReimbService()

# As an employee, I want to be able to submit and review my reimbursement requests

@ec.route('/<username>/home')
def get_user(username):
    return us.get_user_info(username)


@ec.route('/<username>/submit-reimbursement', methods=['PUT'])
def submit_reimb(username):
    json_input = request.get_json()
    amount = json_input['amount']
    submitted = json_input['submission_time']
    type = json_input['type']
    descrip = json_input['description']
    receipt = json_input['receipt']
    author = json_input['username']
    try:
        rs.create_reimb(Reimbursement(amount, submitted, type, descrip, receipt, author))
    except InvalidParamError as e:
        return{
            'message': f"{e}"
        }, 400

@ec.route('/<username>/reimbursements')
def get_all_reimbs_e():
    json_entry = request.get_json()
    if "user" in session:
        try:
            rs.get_all_reimbs(session['user_id'], json_entry['filter_status'], json_entry['filter_type'], cookie['role'])
        except InvalidParamError as e:
            return {
                'message': f"{e}"
            }, 400
    else:
        return redirect(url_for(uc.login))
