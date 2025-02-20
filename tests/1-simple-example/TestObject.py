from typing import Dict, List
from robot.api.logger import info

# semua code untuk TestObject.py digenerate melalui Chat GPT
class TestObject:
    def __init__(self, ip: str):
        self.ip = ip
        self.token = None
        self.users = {
            'ironman': {'password': '1234567890', 'name': 'Tony Stark', 'right': 'user', 'active': True},
            'admin': {'password': '@RBTFRMWRK@', 'name': 'Administrator', 'right': 'admin', 'active': True}
        }
        self.server_version = '1.0.0'

    def authenticate(self, login: str, password: str) -> str:
        info(f'Attempting to authenticate user: {login} with password: {password}')
        user = self.users.get(login.strip())
        if user and user['password'] == password.strip():
            self.token = f'token_{login}'
            info(f'Authentication successful for user: {login}')
            return self.token
        else:
            info(f'Authentication failed for user: {login}')
            raise ValueError('Invalid Password')

    def logout(self, token):
        if token == self.token:
            self.token = None
        else:
            raise ValueError('Invalid Token')

    def get_version(self, token) -> str:
        if token != self.token:
            raise PermissionError('Unauthorized access')
        return self.server_version

    def get_user_id(self, token, login) -> str:
        if token != self.token:
            raise PermissionError('Unauthorized access')
        if login in self.users:
            return f'id_{login}'
        else:
            raise ValueError('User not found')

    def get_user_name(self, token, user_id) -> str:
        if token != self.token:
            raise PermissionError('Unauthorized access')
        login = user_id.replace('id_', '') if user_id else self.token.replace('token_', '')
        user = self.users.get(login)
        if user:
            return user['name']
        else:
            raise ValueError('User not found')

    def get_user(self, token, user_id=None) -> Dict[str, str]:
        if token != self.token:
            raise PermissionError('Unauthorized access')
        login = user_id.replace('id_', '') if user_id else self.token.replace('token_', '')
        user = self.users.get(login)
        if user:
            return user
        else:
            raise ValueError('User not found')

    def get_user_all(self, token) -> List[Dict[str, str]]:
        if token != self.token:
            raise PermissionError('Unauthorized access')
        return list(self.users.values())

    def delete_user(self, token, userid):
        if token != self.token:
            raise PermissionError('Unauthorized access')
        if not userid:
            raise ValueError('User ID is required')
        login = userid.replace('id_', '')
        if login in self.users:
            del self.users[login]
        else:
            raise ValueError('User not found')

    def get_logout(self, token):
        self.logout(token)

    def put_user_password(self, token, new_password, user_id=None):
        if token != self.token:
            raise PermissionError('Unauthorized access')
        login = user_id.replace('id_', '') if user_id else self.token.replace('token_', '')
        if login and login in self.users:
            self.users[login]['password'] = new_password
        else:
            raise ValueError('User not found')

    def put_user_name(self, token, name, user_id=None):
        if token != self.token:
            raise PermissionError('Unauthorized access')
        login = user_id.replace('id_', '') if user_id else self.token.replace('token_', '')
        if login and login in self.users:
            self.users[login]['name'] = name
        else:
            raise ValueError('User not found')

    def put_user_right(self, token, right, user_id):
        if token != self.token:
            raise PermissionError('Unauthorized access')
        if not user_id:
            raise ValueError('User ID is required')
        login = user_id.replace('id_', '')
        if login in self.users:
            self.users[login]['right'] = right
        else:
            raise ValueError('User not found')

    def post_new_user(self, token, name, login) -> str:
        if token != self.token:
            raise PermissionError('Unauthorized access')
        if login in self.users:
            raise ValueError('User already exists')
        self.users[login] = {'password': '', 'name': name, 'right': 'user', 'active': True}
        return f'id_{login}'
