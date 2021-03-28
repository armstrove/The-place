from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_element_by_id():
    try:
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "navbar_tutorialsss"))
             )
    except:
        assert False
    return element

