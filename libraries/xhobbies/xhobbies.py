from libraries.common import act_on_element, capture_page_screenshot
from config import OUTPUT_FOLDER
import time


class Xhobbies():

    def __init__(self, rpa_selenium_instance, credentials: dict):
        self.browser = rpa_selenium_instance  # browser variable in common
        self.xhobbies_url = credentials["url"]
        self.xhobbies_login = credentials["login"]
        self.xhobbies_password = credentials["password"]

    def login(self):
        """
        Login to Xhobbies with Bitwarden credentials.
        """
        try:
            self.browser.go_to(self.xhobbies_url)
            self.input_credentials()
            self.submit_form()
            # capture_page_screenshot(OUTPUT_FOLDER, "Page_Xhobbies_Login")
            print("Success go to xhobbies url", self.xhobbies_url)
        except Exception as e:
            capture_page_screenshot(OUTPUT_FOLDER, "Exception_Xhobbies_Login")
            raise Exception("Login to Xhobbies failed")
    
    def input_credentials(self):
        """
        Function that writes the credentials in the login form.
        """
        self.browser.input_text_when_element_is_visible('//input[@id="CustomerEmail"]', self.xhobbies_login)
        self.browser.input_text_when_element_is_visible('//input[@id="CustomerPassword"]', self.xhobbies_password)
        return
    
    def submit_form(self):
        """
        Function that submits the login form and waits for the main page to load.
        """
        self.browser.click_element('//button[contains(text(), "Ingresar")]')
        time.sleep(5)
        act_on_element('//div[@class="content-header-top"]', "find_element")
        return

