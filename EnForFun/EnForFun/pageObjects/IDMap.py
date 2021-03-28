class IDMap:
    def __init__(self):
        self.IDMap = {
            "NavBar": {
                "Tutorials"   :  "navbar_tutorials",
                "Topics"      :  "navbar_topics",
                "HomePage"    :  "navbar_homePage",
                "LoginButton" :  "login_button"
            }
        }

    def get_id(self,searchArray):
        sub_dict=self.IDMap
        for key in searchArray:
            try:
              sub_dict=sub_dict[key]
            except:
              print("Error: wasn't able to find '" + key + "'")
              return ""
        id=sub_dict
        return id
