from flask import Blueprint, request, session, render_template, redirect, url_for
from service.reimb_service import ReimbService
from model.reimbursement import Reimbursement
from exception.invalid_param import InvalidParamError
import json

fmc = Blueprint('finance_manager_controller', __name__)
rs = ReimbService()

# As a finance manager, I want to be able to view and approve reimbursement requests

@fmc.route('/fm/reimbursements')
def get_all_reimbs_fm():
    if "user" in session:
        print("in fmc /fm/reimbursements:: session: ", session)
        status = request.args.get('filter-status')
        filter_type = request.args.get('filter-type')
        if status == 'all-statuses':
            status = None
        if filter_type == 'all-types':
            filter_type = None
        try:
            reimbs = rs.get_all_reimbs(None, status, filter_type, session['user']['role'])
            to_return = {"reimbs": []}

            for re in reimbs:
                to_return["reimbs"].append(re.to_dict())

            json_return = json.dumps(to_return)
            # json_return = json_return.replace("'",'"')
            print("to_return from fmc : ", json_return)
            return json_return
        except InvalidParamError as e:
            return {
                       'message': f"{e}"
                   }, 400
    else:
        return redirect(url_for('login.html'))


@fmc.route('/fm/home')
def finance_manager_home():
    if "user" in session:
        return session
    else:
        return "problem"