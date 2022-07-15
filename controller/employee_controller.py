from flask import Blueprint, request, make_response
from service.user_service import UserService
from service.reimb_service import ReimbService
from model.reimbursement import Reimbursement
from model.user import User
from exception.invalid_param import InvalidParamError

ec = Blueprint('employee_controller', __name__)
us = UserService()
rs = ReimbService()

ec.route('/login', methods=['POST'])
def login():
    json_input = request.get_json()
    usn = json_input['username']
    pwd = json_input['password']
    try:
        resp = make_response()
        resp.set_cookie('login', us.check_password(usn, pwd), 60*60*2)
        return resp
    except InvalidParamError as e:
        return{
            "message": f"{e}"
        }, 400



ec.route('/<username>/home')
def get_user(username):
    return us.get_user_info(username)

ec.route('/<username>/submit-reimbursement', methods=['PUT'])
def submit_reimb(username):
    json_input = request.get_json()

