from libraries.common import log_message, capture_page_screenshot, browser
from libraries.xhobbies.xhobbies import Xhobbies
from config import OUTPUT_FOLDER


class Process:
    def __init__(self, credentials: dict):
        log_message("Initialization")
        prefs = {
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_settings.popups": 0,
            "directory_upgrade": True,
            "download.default_directory": OUTPUT_FOLDER,
            "plugins.always_open_pdf_externally": True,
            "download.prompt_for_download": False
        }
        browser.open_available_browser(preferences = prefs)#browser_selection=["firefox"]
        browser.set_window_size(1920, 1080)
        browser.maximize_browser_window()
        xhobbies = Xhobbies(browser, credentials["Xhobbies"])  # crear xhobbies login
        xhobbies.login()



    def start(self):
        log_message("Macro Step 1")
        log_message("Macro Step 2")
        log_message("Macro Step 3")

    def finish(self):
        capture_page_screenshot(OUTPUT_FOLDER, "Xhobbies_Login")
        log_message("DW Process Finished")
        browser.close_browser()
