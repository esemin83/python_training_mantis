from fixture.session import SessionHelper
from fixture.project import Project
from fixture.james import James
from selenium import webdriver
from fixture.singup import SingupHelper
from fixture.mail import MailHelper
from fixture.soap import SoapHelper


class Application:

        def __init__(self, browser, config):
            if browser == "firefox":
                self.wd = webdriver.Firefox()
            elif browser == "chrome":
                self.wd = webdriver.Chrome()
            elif browser == "ie":
                self.wd = webdriver.Ie()
            else:
                raise ValueError("Unrecognized browser %s" % browser)
            #self.wd.implicitly_wait(5)
            self.session = SessionHelper(self)
            self.pr = Project(self)
            self.james = James(self)
            self.singup = SingupHelper(self)
            self.mail = MailHelper(self)
            self.soap = SoapHelper(self)
            self.config = config
            self.base_url = config['web']['baseUrl']
            self.wsdl = config['soap']['wsdl']

        def is_valid(self):
            try:
                self.wd.current_url
                return True
            except:
                return False

        def open_home_page(self):
                # open home page
                wd = self.wd
                wd.get(self.base_url)

        def destroy(self):
                self.wd.quit()
