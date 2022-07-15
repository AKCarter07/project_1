from flask import Blueprint, request, make_response
from service.user_service import UserService
from service.reimb_service import ReimbService
from model.reimbursement import Reimbursement
from model.user import User
from exception.invalid_param import InvalidParamError

uc = Blueprint('user_controller', __name__)
us = UserService()
rs = ReimbService()

uc.route('/setcookie', methods=['POST', 'GET'])
def setcookie(cookie_data):
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response("Setting a cookie")
        resp.set_cookie('login', cookie_data)
        return resp

uc.route('/getcookie')
def getcookie():
    dict = request.cookies.get('login')
    return dict

uc.route('/login', methods=['POST'])
def login():
    json_input = request.get_json()
    usn = json_input['username']
    pwd = json_input['password']
    try:
        setcookie(us.check_password(usn, pwd))
    except InvalidParamError as e:
        return {
                 "message": f"{e}"
               }, 400
