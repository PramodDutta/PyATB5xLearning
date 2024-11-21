def add_security(func):

    def wrapper():
        print("1.Before the function is called.")
        print("2.Add Helmet, Dashcash, gloves, knee guards, License")
        func() # # driving_scooty()
        print("3.After the function is called.")
        print("4.Secure Driving, Leave all the items")

    return wrapper()

@add_security
def drive_ola_scooter():
    print("ola")


@add_security
def driving_scooty():
    print("Normal Function!!")
    print("I am driving a Scooty")

