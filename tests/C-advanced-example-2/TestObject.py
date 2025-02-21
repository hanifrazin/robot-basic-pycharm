from typing import Dict, List, Optional

# semua code di TestObject pure di geneare by AI Chat GPT
class TestObject:
    def __init__(self, ip: str):
        """
        Initializes the TestObject with the given IP address.
        """
        self.ip = ip
        self.users: Dict[str, Dict] = {
            "admin": {"name": "Administrator", "login": "admin", "password": "@RBTFRMWRK@", "right": "admin", "active": True, "id": "1"},
            "hulk": {"name": "Hulk", "login": "hulk", "password": "Hulk...SMASH!", "right": "user", "active": True, "id": "2"},
            "dr.strange": {"name": "Stephen Strange", "login": "dr.strange", "password": "magic", "right": "user", "active": True, "id": "3"},
            "captain": {"name": "Steve Rogers", "login": "captain", "password": "shield", "right": "user", "active": True, "id": "4"},
            "ironman": {"name": "Tony Stark", "login": "ironman", "password": "1234567890", "right": "user", "active": True, "id": "5"},
            "spider": {"name": "Peter Parker", "login": "spider", "password": "123spiderman321", "right": "user", "active": True, "id": "6"}
        }
        self.version = "1.0"
        self.tokens: Dict[str, str] = {}  # Store tokens for each user

    def authenticate(self, login: str, password: str) -> str:
        """
        Authenticates the user and returns a token.
        """
        for user_id, user in self.users.items():
            if user["login"] == login and user["password"] == password:
                token = f"{login}_token"  # Simplified token generation
                self.tokens[login] = token
                return token
        return None

    def logout(self, token: str):
        """
        Logs out the user by removing the token.
        """
        for login, stored_token in self.tokens.items():
            if stored_token == token:
                del self.tokens[login]
                return
        raise ValueError("Invalid token")

    def get_version(self, token: str) -> str:
        """
        Returns the version of the API.
        """
        self._validate_token(token)
        return self.version

    def get_user_id(self, token: str, login: str) -> str:
        """
        Returns the user ID based on the login.
        """
        self._validate_token(token)
        for user_id, user in self.users.items():
            if user["login"] == login:
                return user_id
        return None

    def get_user_name(self, token: str, user_id: str = None) -> str:
        """
        Returns the user's full name. If user_id is None, returns the name of the user associated with the token.
        """
        self._validate_token(token)
        if user_id is None:
            login = self._get_login_from_token(token)
            for user_id, user in self.users.items():
                if user["login"] == login:
                    return user["name"]
            return None
        elif user_id in self.users:
            return self.users[user_id]["name"]
        else:
            return None

    def get_user(self, token: str, user_id: str = None) -> Dict[str, str]:
        """
        Returns the user details. If user_id is None, returns the details of the user associated with the token.
        """
        self._validate_token(token)
        if user_id is None:
            login = self._get_login_from_token(token)
            for user_id, user in self.users.items():
                if user["login"] == login:
                    return user
            return None
        elif user_id in self.users:
            return self.users[user_id]
        else:
            return None

    def get_user_all(self, token: str) -> List[Dict[str, str]]:
        """
        Returns a list of all users.
        """
        self._validate_token(token)
        return list(self.users.values())

    def delete_user(self, token: str, userid: str):
        """
        Deletes a user.
        """
        self._validate_token(token)
        if userid in self.users:
            del self.users[userid]
        else:
            raise ValueError("User not found")

    def get_logout(self, token: str):
        """
        Logs out the user.
        """
        self.logout(token)

    def put_user_password(self, token: str, new_password: str, user_id: str = None):
        """
        Updates the user's password. If user_id is None, updates the password of the user associated with the token.
        """
        self._validate_token(token)
        if user_id is None:
            login = self._get_login_from_token(token)
            for user_id, user in self.users.items():
                if user["login"] == login:
                    self.users[user_id]["password"] = new_password
                    return
        elif user_id in self.users:
            self.users[user_id]["password"] = new_password
        else:
            raise ValueError("User not found")

    def put_user_name(self, token: str, name: str, user_id: str = None):
        """
        Updates the user's name. If user_id is None, updates the name of the user associated with the token.
        """
        self._validate_token(token)
        if user_id is None:
            login = self._get_login_from_token(token)
            for user_id, user in self.users.items():
                if user["login"] == login:
                    self.users[user_id]["name"] = name
                    return
        elif user_id in self.users:
            self.users[user_id]["name"] = name
        else:
            raise ValueError("User not found")

    def put_user_right(self, token: str, right: str, user_id: str):
        """
        Updates the user's rights.
        """
        self._validate_token(token)
        if user_id in self.users:
            self.users[user_id]["right"] = right
        else:
            raise ValueError("User not found")

    def post_new_user(self, token: str, name: str, login: str) -> str:
        """
        Creates a new user and returns the new user's ID.
        """
        self._validate_token(token)
        new_user_id = str(len(self.users) + 1)
        self.users[new_user_id] = {
            "name": name,
            "login": login,
            "password": "default_password",  # You should set a password later
            "right": "user",
            "active": True,
            "id": new_user_id
        }
        return new_user_id

    def _validate_token(self, token: str):
        """
        Validates the token.
        """
        if token not in self.tokens.values():
            raise PermissionError("Invalid token")

    def _get_login_from_token(self, token: str) -> str:
        """
        Retrieves the login from the token.
        """
        for login, stored_token in self.tokens.items():
            if stored_token == token:
                return login
        raise ValueError("Invalid token")
