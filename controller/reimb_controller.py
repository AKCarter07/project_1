from flask import Blueprint, request
from service.reimb_service import ReimbService

rc = Blueprint('reimb_controller', __name__)
rs = ReimbService()

# As an employee, I want to be able to submit and review my reimbursement requests
# As a finance manager, I want to be able to view and approve reimbursement requests


