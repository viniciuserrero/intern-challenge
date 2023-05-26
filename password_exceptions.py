class ShortPasswordException(Exception):
    """
    This exception must be used when the password size is lower than the minimum
    """

    def __init__(self, min_size: int = 8):
        self.msg = f"Password is too small. Must have at least {min_size} characters"

    def __str__(self) -> str:
        return self.msg


class MissingCharacterException(Exception):
    """
    This exception must be used when the password is missing one of the following:
    - Lowercase characters
    - Uppercase characters
    - Digits
    - Special characters
    """

    def __init__(self, param):
        self.msg = f"Password must contain at least one {param}"

    def __str__(self) -> str:
        return self.msg


class InvalidCharacterException(Exception):
    """
    This exception must be used when the password contains an invalid character
    """

    def __init__(self):
        self.msg = "Password contains an invalid character"

    def __str__(self) -> str:
        return self.msg


class InsufficientScoreException(Exception):
    """
    This exception must be used when the password score is lower than the minimum
    """

    def __init__(self, score: int, min_score: int = 16):
        self.msg = f"Password score is too low({score}). Must be at least {min_score}"

    def __str__(self) -> str:
        return self.msg
