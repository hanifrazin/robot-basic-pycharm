from TestObject import TestObject
from robot.api.logger import info, debug, trace, console

class CustomLibrary:
    '''This is a user written keyword library.
    These libraries can be pretty handy for more complex tasks an typically
    more efficiant to implement compare to Resource files.

    However, they are less simple in syntax and less transparent in test protocols.

    The TestObject object (t) has the following public functions:

    class TestObject:
        def authenticate(self, login: str, password: str) -> str: ...
        def logout(self, token): ...
        def get_version(self, token) -> str: ...
        def get_user_id(self, token, login) -> str: ...
        def get_user_name(self, token, user_id) -> str: ...
        def get_user(self, token, user_id=None) -> Dict[str, str]: ...
        def get_user_all(self, token) -> List[Dict[str, str]]: ...
        def delete_user(self, token, userid): ...
        def get_logout(self, token): ...
        def put_user_password(self, token, new_password, user_id=None): ...
        def put_user_name(self, token, name, user_id=None): ...
        def put_user_right(self, token, right, user_id): ...
        def post_new_user(self, token, name, login) -> str: ...
    '''

    ROBOT_LIBRARY_SCOPE = 'SUITE'

    def __init__(self) -> None:
        self._session = None
        self.login = ''
        self.password = ''
        self._connection: TestObject = None

    def connect(self,ip):
        self._connection = TestObject(ip)

    def disconnect(self):
        self._connection = None

    @property
    def connection(self):
        if not self._connection:
            raise SystemError('No connection established! Connect to server first')
        return self._connection

    @property
    def session(self):
