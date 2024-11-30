class Bank:
    def __init__(self, account_number, balance):
        self.balance = balance  # Public
        self.__account_number = account_number  # Private

    def check_balance(self):
        print(self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount

    def public_function(self):
        self.__internal_private_method();

    def show_me_account_number(self, is_auth):
        if is_auth == True:
            print(self.__account_number)
        else:
            print("Not Allowed!")

    def __internal_private_method(self):
        print("Private Method, can be access by only Class")


icici = Bank(9876543210, 100)
icici.deposit(100)
icici.check_balance()
print(icici.balance)
# print(icici.__account_number)
icici.show_me_account_number(False)
# icici.__internal_private_method()
