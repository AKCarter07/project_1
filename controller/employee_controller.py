from flask import Blueprint, request, session, redirect, url_for
from service.user_service import UserService
from service.reimb_service import ReimbService
from model.reimbursement import Reimbursement
from model.user import User
from exception.invalid_param import InvalidParamError
from controller.user_controller import uc
import json
import datetime

ec = Blueprint('employee_controller', __name__)
us = UserService()
rs = ReimbService()

# As an employee, I want to be able to submit and review my reimbursement requests


@ec.route('/e/reimbursements')
def get_all_reimbs_e():
    if "user" in session:
        # print("in ec /e/reimbursements:: session ~~ ", session)
        status = request.args.get('filter-status')
        filter_type = request.args.get('filter-type')
        if status == 'all-statuses':
            status = None
        if filter_type == 'all-types':
            filter_type = None
        try:
            reimbs = rs.get_all_reimbs(session['user']['id'], status, filter_type, session['user']['role'])
            to_return = {"reimbs": []}

            for re in reimbs:
                to_return["reimbs"].append(re.to_dict())

            # print("to_return from ec : ", to_return)
            return to_return, 201
        except InvalidParamError as e:
            return {
                'message': f"{e}"
            }, 400
    else:
        return {
            'message': 'must be logged in'
        }, 401


@ec.route('/e/reimbursement', methods=['POST'])
def submit_reimb():
    if "user" in session:
        print("ec.route/e/reimbursements ~~ ", session)
        time = datetime.datetime.now()
        json_input = request.get_json()
        reimb = Reimbursement(json_input['amount'], time, json_input['type'], json_input['description'], None,
                              session['user']['id'])
        print(reimb)
        return rs.create_reimb(reimb), 201
    else:
        return {
             'message': 'must be logged in'
        }, 401

