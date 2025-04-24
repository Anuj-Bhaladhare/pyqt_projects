

class AuthService:
    @staticmethod
    def authenticate(email, password):
        # Validate from DB or API
        return email == "admin" and password == "123"