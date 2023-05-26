from variation_checker import VariationChecker
from common_password_checker import CommonPasswordChecker


class ScoreCalculation:
    """
    This class contains the code to calculate the score.
    Passwords with score lower than 16 are invalid
    """

    def __init__(self, password: str) -> None:
        self.password = password
        self.checker = VariationChecker(password)
        self.common_checker = CommonPasswordChecker(password).check_common()
        self.score = 0

    def check_score_characters(self):
        # Write your code here
        return self.score
