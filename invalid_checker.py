from password_exceptions import InvalidCharacterException


class InvalidChecker:
    """
    This class should contain the code to check
    if the password contains any invalid characters
    """

    def __init__(self, password: int) -> None:
        special_chars = "!$%&\()*+-/?@_"
        if any(char not in special_chars for char in password):
            raise InvalidCharacterException
