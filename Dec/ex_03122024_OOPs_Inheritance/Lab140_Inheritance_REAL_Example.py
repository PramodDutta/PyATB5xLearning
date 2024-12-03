class BaseTest:
    def open_browser(self):
        print("Starting the browser")

    def read_from_excel(self):
        print("Read from Excel")

    def close_browser(self):
        print("Close browser")


class TestCase1(BaseTest):

    def test_positive(self):
        self.open_browser()
        print("Test case P1 Executed!!")
        self.read_from_excel()
        self.close_browser()

    def test_negative(self):
        self.open_browser()
        print("Test case N1 Executed!!")
        self.close_browser()


class TestCase2(BaseTest):

    def test_2(self):
        self.open_browser()
        print("Test case P2 Executed!!")
        self.close_browser()


class TestCase3(BaseTest):

    def test_3(self):
        self.open_browser()
        print("Test case P3 Executed!!")
        self.close_browser()