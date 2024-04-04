import re

class EmailAddressParser:
    """Parses a string of email addresses into an array of unique, sorted email addresses."""

    def __init__(self, input_email_addresses):
        """Initializes the parser with a string of email addresses."""
        self.input_email_addresses = input_email_addresses

    def parse(self):
        """Parses the input string into an array of unique, sorted email addresses."""

        # Split the input string into individual email addresses using a regular expression.
        parsed_email_addresses = re.split(r"[ ,]", self.input_email_addresses)

        # Convert the list to a sorted set to remove duplicates and sort the addresses alphabetically.
        parsed_email_addresses = sorted(set(parsed_email_addresses))

        return parsed_email_addresses
