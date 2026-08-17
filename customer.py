class Customer:
    def __init__(self, customer_id, name, password):
        self.customer_id=customer_id
        self.name=name
        self.password=password
        
    def print_details(self):
        print("------CUSTOMER DETAILS---------")
        print("Customer ID=", self.customer_id)
        print("Name=", self.name)
        
    def check_password(self, password):
        return self.password == password 
        
    