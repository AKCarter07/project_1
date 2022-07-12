class Reimbursment:
    def __init__(self, id, amount, submitted, resolved, status, type, descrip, receipt, author, resolver):
        self.reimb_id = id
        self.amount = amount
        self.submitted = submitted
        self.resolved = resolved
        self.status = status
        self.type = type
        self.descrip = descrip
        self.receipt = receipt
        self.author = author
        self.resolver = resolver

