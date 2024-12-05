class ExcelReader:

    @staticmethod
    def read_from_excel():
        print("Reading from excel")

class MYSQLDBConnection:

    @staticmethod
    def readMySQLFile():
        print("Reading from MySQL")


class TC1:
    static_var = 10


    @staticmethod
    def testcase():
        MYSQLDBConnection.readMySQLFile()
        ExcelReader.read_from_excel()
        print(TC1.static_var) # Shared among all instances of the class




TC1.testcase()