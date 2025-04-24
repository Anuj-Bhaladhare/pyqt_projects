from views.home_view import HomeScreenView
from views.login_view import LoginScreenView
from views.sing_up_screen import SingupScreenView
from views.user_screen import UserScreenView


class MainController:
    def __init__(self, view):
        self.view = view
        self.home_screen = None
        self.login_screen = None
        self.sing_up_screen = None
        self.user_screen = None

########################################################################
#################### DEFINE CONNECTION HERE ############################
    def setup_connection(self):
        # ------------- PushButton ---------------
        self.view.home_push_button.clicked.connect(self.load_home_screen)
        self.view.login_push_button.clicked.connect(self.load_login_screen)
        self.view.singup_push_button.clicked.connect(self.load_sing_up_screen)
        self.view.user_push_button.clicked.connect(self.load_user_screen)
    

#########################################################################
#################### DEFINE FUNCTION HERE ###############################
    
    # ---------------- Click the Home Button ---------------- 
    def load_home_screen(self):
        # only load once
        if not self.home_screen:
            self.home_screen = HomeScreenView()
            self.view.main_body_container.addWidget(self.home_screen)

        index = self.view.main_body_container.indexOf(self.home_screen)
        self.view.main_body_container.setCurrentIndex(index)


    #  ---------------- Click the Login Button ---------------- 
    def load_login_screen(self):
        # only load once
        if not self.login_screen:
            self.login_screen = LoginScreenView()
            self.view.main_body_container.addWidget(self.login_screen)

        index = self.view.main_body_container.indexOf(self.login_screen)
        self.view.main_body_container.setCurrentIndex(index)


    #  ---------------- Click the Sing Up Button ---------------- 
    def load_sing_up_screen(self):
        # only load once
        if not self.sing_up_screen:
            self.sing_up_screen = SingupScreenView()
            self.view.main_body_container.addWidget(self.sing_up_screen)

        index = self.view.main_body_container.indexOf(self.sing_up_screen)
        self.view.main_body_container.setCurrentIndex(index)


    #  ---------------- Click the Users Button ---------------- 
    def load_user_screen(self):
        # only load once
        if not self.user_screen:
            self.user_screen = UserScreenView()
            self.view.main_body_container.addWidget(self.user_screen)

        index = self.view.main_body_container.indexOf(self.user_screen)
        self.view.main_body_container.setCurrentIndex(index)

