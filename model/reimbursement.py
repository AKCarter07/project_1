class Reimbursement:
    def __init__(self, amount, submitted, type, descrip, receipt, author):
        self.reimb_id = None
        self.amount = amount
        self.submitted = submitted
        self.resolved = None
        self.status = 'pending'
        self.type = type
        self.descrip = descrip
        self.receipt = receipt
        self.author = author
        self.resolver = None

    def to_dict(self):
        return {
            'reimbursement id': self.reimb_id,
            'amount': self.amount,
            'type': self.type,
            'description': self.descrip,
            'receipt': self.receipt,
            'submitter id': self.author,
            'status': self.status,
            'date submitted': self.submitted,
            'date resolved': self.resolved,
            'resolver id': self.resolver
        }

    def set_id(self, id):
        self.reimb_id = id

    def set_resolved(self, resolved):
        self.resolved = resolved
        return f"Reimbursement {self.reimb_id} has been resolved."

    def set_status(self, status):
        self.status = status
        return f"Reimbursement {self.reimb_id} has been {self.status}."

    def set_resolver(self, resolver):
        self.resolver = resolver
        return f"Reimbursement {self.reimb_id} has been resolved by {self.resolver}."
