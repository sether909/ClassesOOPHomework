# FoodProgram.py
import FoodClass as fc

# This dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid']
dict = {
    'trans1': ['2/15/2023', 'The Lone Patty', 17, 569],
    'trans2': ['2/15/2023', 'The Octobreakfast', 18, 569],
    'trans3': ['2/15/2023', 'The Octoveg', 16, 570],
    'trans4': ['2/15/2023', 'The Octoburger', 20, 570],
}

# Customer information
# Manually toggle which customer to use for each report.
customers = [
    fc.Customer(570, 'Danni Sellyar', '97 Mitchell Way Hewitt Texas 76712', 'dsellyarft@gmpg.org', '254-555-9362', False),
    #fc.Customer(569, 'Aubree Himsworth', '1172 Moulton Hill Waco Texas 76710', 'ahimsworthfs@list-manage.com', '254-555-2273', True)
]

# Create Transaction instances from the dictionary
transactions = [fc.Transaction(*details) for details in dict.values()]

def create_report(customer, transactions):
    
    print(f"Customer Name: {customer.get_name()}")
    print(f"Phone: {customer.get_phone()}")
    
    total_cost = 0
    for transaction in transactions:
        if transaction.get_customerid() == customer.get_customerid():
            print(f"Order Item: {transaction.get_item_name()} Price: ${transaction.get_cost():.2f}")
            total_cost += transaction.get_cost()
    
    print(f"Total Cost: ${total_cost:.2f}")

    if customer.get_member_status():
        discount = total_cost * 0.2
        total_cost -= discount
        print(f"Member Discount: ${discount:.2f}")
        print(f"Total cost after discount: ${total_cost:.2f}")
    
# Generate report for each customer
for customer in customers:
    create_report(customer, transactions)
