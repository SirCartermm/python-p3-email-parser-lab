import pytest

def test_parse_csv():
    email_addresses = "john@doe.com, person@somewhere.org"
    parser = EmailAddressParser(email_addresses)

    assert parser.parse() == ["john@doe.com", "person@somewhere.org"]

def test_parse_space():
    email_addresses = "john@doe.com person@somewhere.org"
    parser = EmailAddressParser(email_addresses)

    assert parser.parse() == ["john@doe.com", "person@somewhere.org"]

def test_parse_unique():
    email_addresses = "john@doe.com, john@doe.com, person@somewhere.org"
    parser = EmailAddressParser(email_addresses)

    assert parser.parse() == ["john@doe.com", "person@somewhere.org"]

def test_parse_sorted():
    email_addresses = "person@somewhere.org, john@doe.com"
    parser = EmailAddressParser(email_addresses)

    assert parser.parse() == ["john@doe.com", "person@somewhere.org"]
