
class LoginController:
    def __init__(self, view):
        self.view = view

########################################################################
#################### DEFINE CONNECTION HERE ############################
    def setup_connection(self):
        # ------------- PushButton ---------------
        self.view.navigate_singup_btn.clicked.connect(self.navigate_singup_page)
        self.view.login_btn.clicked.connect(self.user_login)
    

#########################################################################
#################### DEFINE FUNCTION HERE ###############################
    
    # ---------------- Click the Home Button ---------------- 
    def navigate_singup_page(self):
        print("navigate_singup_page navigate_singup_page navigate_singup_page")


    def user_login(self):
        print("user_login user_login user_login")
