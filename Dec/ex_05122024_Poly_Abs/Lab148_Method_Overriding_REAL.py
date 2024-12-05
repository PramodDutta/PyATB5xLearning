class OldBrowser:

    def start_browser(self):
        print("IE browser is starting")

    def stop_browser(self):
        print("IE browser is Closing")



class Chrome(OldBrowser):

    def start_browser(self):
        super().start_browser() # Parent Start browser also.
        print("Better Chrome browser is starting...")

    def stop_browser(self):
        print("Better Chrome browser is Stopping...")

    pass


obj_ref = Chrome()
obj_ref.start_browser()
obj_ref.stop_browser()
