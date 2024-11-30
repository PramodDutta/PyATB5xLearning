# Web Automation - Selenium
# Page - You are going automate

class VWOLoginPage:

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "pramod@gmail.com" and self.password == "Pass123":
            print("Allowed, Login Sucess")
        else:
            print("Login Failed")


# email = # Read from test data - Excel,CSV or Env file
# password = #Read from test data -Excel.CSV or Env file

# vwo_obj = VWOLoginPage(email, password)
# vwo_obj.login_confirm()

pramod = VWOLoginPage("pramod@gmail.com", "Pass123")
pramod.login_confirm()