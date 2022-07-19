from flask import Blueprint, request, session, redirect, url_for, render_template
from service.user_service import UserService
from service.reimb_service import ReimbService
from model.reimbursement import Reimbursement
from model.user import User
from exception.invalid_param import InvalidParamError

uc = Blueprint('user_controller', __name__)
us = UserService()
rs = ReimbService()

@uc.route('/')
def blank():
    return "Hello World"


@uc.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        json_input = request.get_json()
        usn = json_input['username']
        pwd = json_input['password']
        try:
            key = us.check_password(usn, pwd)
            session["user"] = key
            return session["user"], 200
            # if session['role'] == "employee":
            #     return redirect(url_for("ec.employee-home"))
            # elif session['role'] == "finance manager":
            #     return redirect(url_for("fmc.finance-manager-home"))
        except InvalidParamError as e:
            return{
                "message": f"{e}"
            }, 400
    else:
        if "user" in session:
            return "already had cookie"
            # if session['role'] == "employee":
            #     return redirect(url_for("ec.employee_home"))
            # elif session['role'] == "finance manager":
            #     return redirect(url_for("fmc.finance_manager_home"))
    return render_template("login.html")

@uc.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return {
        "message": "Successfully logged out"
    }, 200


@uc.route('/home')
def home():
    if "user" in session:
        user = session ["user"]
        return f"<h1>{user}</h1>"
    else:
        return session