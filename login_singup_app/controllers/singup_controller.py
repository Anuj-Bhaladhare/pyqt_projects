
class SingUpController:
    def __init__(self, view):
        self.view = view

########################################################################
#################### DEFINE CONNECTION HERE ############################
    def setup_connection(self):
        # ------------- PushButton ---------------
        self.view.navigate_login_btn.clicked.connect(self.navigate_login_page)
        self.view.sing_up_btn.clicked.connect(self.user_sing_up)
    

#########################################################################
#################### DEFINE FUNCTION HERE ###############################
    
    def navigate_login_page(self):
        print("navigate_login_page navigate_login_page navigate_login_page")


    def user_sing_up(self):
        print("user_sing_up user_sing_up user_sing_up")
