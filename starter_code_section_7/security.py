from werkzeug.security import safe_str_cmp
from starter_code_section_7.models.user import UserModel


def authenticate(username: str, password: str):
    """
    Method that gets called when a user calls the "/auth" endpoint
    with their username and password
    :param username: User's name in string format.
    :param password: User's un-encrypted password in string format.
    :return: A user if authentication was successful, None otherwise
    """

    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user
    else:
        return None

    
def identity(payload):
    """
    Function that gets called when user has already authenticated,
    and Flask-JWT verified their authorization header is correct.
    :param payload: A dictionary with 'identity' key, which is the user id.
    :return: A UserModel object.
    """

    user_id = payload['identity']
    return UserModel.find_by_id(user_id)

