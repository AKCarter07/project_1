from flask import Blueprint, request, session, redirect, url_for, render_template
from service.user_service import UserService
from service.reimb_service import ReimbService
from model.reimbursement import Reimbursement
from model.user import User
from exception.invalid_param import InvalidParamError
from controller.employee_controller import ec
from controller.finance_manager_controller import fmc

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
            session["user"] = us.check_password(usn, pwd)
            if session['role'] == "employee":
                return redirect(url_for("ec.employee-home"))
            elif session['role'] == "finance manager":
                return redirect(url_for("fmc.finance-manager-home"))
        except InvalidParamError as e:
            return{
                "message": f"{e}"
            }, 400
    else:
        if "user" in session:
            if session['role'] == "employee":
                return redirect(url_for("ec.employee-home"))
            elif session['role'] == "finance manager":
                return redirect(url_for("fmc.finance-manager-home"))
        return render_template("login.html")

@uc.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


@uc.route('/home')
def home():
    if "user" in session:
        user = session ["user"]
        return f"<h1>{user}</h1>"
