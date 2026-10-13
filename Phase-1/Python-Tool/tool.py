#!/usr/bin/env python3
# Password Generator
# Creates random strong passwords. The user can choose the length,
# how many to make, and whether to include symbols.

import argparse
import secrets
import string
import sys

MIN_LENGTH = 8
MAX_LENGTH = 128


# Builds the set of characters the password can use
def build_characters(use_symbols):
    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += string.punctuation
    return characters


# Builds one random password of the given length
def generate_password(length, use_symbols=True):
    characters = build_characters(use_symbols)
    password = ""
    for i in range(length):
        password += secrets.choice(characters)
    return password


# Stops with an error if the length or count is not acceptable
def check_values(length, count):
    if length < MIN_LENGTH or length > MAX_LENGTH:
        raise ValueError(f"length must be between {MIN_LENGTH} and {MAX_LENGTH}")
    if count < 1 or count > 50:
        raise ValueError("count must be between 1 and 50")


# Reads the options typed by the user and runs the tool
def main():
    parser = argparse.ArgumentParser(description="Random password generator")
    parser.add_argument("-l", "--length", type=int, default=12,
                        help="password length (default 12)")
    parser.add_argument("-c", "--count", type=int, default=1,
                        help="how many passwords to make (default 1)")
    parser.add_argument("--no-symbols", action="store_true",
                        help="use only letters and numbers")
    args = parser.parse_args()

    try:
        check_values(args.length, args.count)
    except ValueError as error:
        print("Error:", error)
        sys.exit(1)

    print(f"Generated {args.count} password(s) of length {args.length}:")
    for i in range(args.count):
        print("  " + generate_password(args.length, not args.no_symbols))


main()
