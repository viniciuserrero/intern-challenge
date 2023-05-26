# Password Validator

This tool will receive a password using the argparse module and analyze it, checking if it's valid and giving a score.

## Instructions

Dear candidate,

Thank you for taking the time to participate in this technical challenge. We would like to inform you that the code provided for this challenge has been modified to remove certain portions and include intentional bugs. This has been done to test your problem-solving skills and ability to debug code.

To get started, please read the following instructions carefully:

1. Fork this repository
2. Clone your forked repository in your local machine.
3. Open the code in your preferred development environment.
4. Read the docstrings in each file to understand the role of every function
5. Please note that the code has been modified to include intentional bugs. These bugs may cause errors or unexpected behavior when running the code. Your task is to identify and fix these bugs.
6. In addition to the bugs, some portions of the code have been removed. You may need to write your own code to replace these missing portions. Please make sure that your solution follows the requirements outlined in the challenge prompt.
7. Once you have fixed all the bugs and completed the missing portions, please test your solution thoroughly to ensure that it is working correctly.
8. Upload your changes in your forked repository.

## Expected behavior

- This code must be able to run in Python 3.11

- The code should receive the password as an argument, printing the score if it's a valid password and raising an Exception if it isn't.

- The exceptions are located in the `password_exceptions.py` file. Please use them accordingly

## Definitions

- Alphanumerical characters:
  - Lowercase characters: `abcdefghijklmnopqrstuvwxyz`
  - Uppercase characters: `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
  - Digits: `0123456789`
- Special characters: `!$%&\()*+-/?@_`

## Score calculation

- Alphanumerical characters (+1 point per character)
- Special characters (+3 points per character)
- Common words (-8 points penalty, independent of the number of common words found)
- Consecutive Repetitive characters (-2 points per repetition)
  - This is an example of a password containing two of these repetitions **(in bold)**: 9898!E**yyy**98rhwq9**88**
  - Each repetition will inflict a two point penalty, resulting in a password score of 16

Only passwords with $score \geq 16$ are valid

## Examples

### Valid

The following input:

```bash
python password_validator.py --password "98Eyq98rhwq98+"
```

should return the following output:

```text
Checking for invalid characters
Checking the password length
Checking for common words
Checking for invalid characters
----
Valid password
Score: 16
```

### Invalid

```bash
python password_validator.py --password "98Eyq98rhwq98"
```

should return the following exception:

```text
password_exceptions.MissingCharacterException: Password must contain at least one special character
```
