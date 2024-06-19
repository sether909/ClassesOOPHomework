
class Customer:
    def __init__(self, _customerid, _name, _address, _email, _phone, _member_status):
        self.customerid = _customerid
        self.name = _name
        self.address = _address
        self.email = _email
        self.phone = _phone
        self.member_status = _member_status

    def get_customerid(self):
        return self.customerid

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def get_member_status(self):
        return self.member_status


class Transaction:
    def __init__(self, _date, _item_name, _cost, _customerid):
        self.date = _date
        self.item_name = _item_name
        self.cost = _cost
        self.customerid = _customerid

    def get_date(self):
        return self.date

    def get_item_name(self):
        return self.item_name

    def get_cost(self):
        return self.cost

    def get_customerid(self):
        return self.customerid
