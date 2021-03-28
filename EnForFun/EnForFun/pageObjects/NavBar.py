from pageObjects import Page


class NavBar(Page.Page):
    def __init__(self, driver):
        super().__init__(driver)
        # self.tutorial_element=driver.get

    def click_on_tutorials(self):
        #navbar_tutorials = self.get_element_by_id(id="navbar_tutorials")
        navbar_tutorials = self.get_element_by_id(id=self.ObjectMap.get_id(["NavBar","Tutorials"]))
        navbar_tutorials.click()

    def click_on_topics(self):
        navbar_tutorials = self.get_element_by_id(id=self.ObjectMap.get_id(["NavBar","Topics"]))
        navbar_tutorials.click()

    def click_on_home(self):
        navbar_tutorials = self.get_element_by_id(id=self.ObjectMap.get_id(["NavBar","HomePage"]))
        navbar_tutorials.click()

    def check_tutorials_loaded(self):
        navbar_tutorials = self.get_element_by_id(id=self.ObjectMap.get_id(["NavBar","Tutorials"]))
        navbar_tutorials.click()

    def check_topic_loaded(self,class_name):
        self.get_element_by_class_name(class_name=class_name)

    def click_on_login(self):
        login = self.get_element_by_id(id=self.ObjectMap.get_id(["NavBar","LoginButton"]))
        login.click()

