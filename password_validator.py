import argparse
from length_checker import LengthChecker
from invalid_checker import InvalidChecker
from score_calculation import ScoreCalculation
from common_password_checker import CommonPasswordChecker


def validate_password(pwd):
    print("Checking for invalid characters")
    InvalidChecker(pwd)

    print("Checking the password length")
    LengthChecker(pwd)

    print("Checking for common words")
    CommonPasswordChecker(pwd).check_common()

    print("Checking for invalid characters")
    score = ScoreCalculation(pwd).check_score_characters()

    print("----")
    print(f"Valid password")
    print(f"Score: {score}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    pwd = parser.parse_args().password
    validate_password(pwd)
