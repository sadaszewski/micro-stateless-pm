#
# Copyright (C) lesspass project
# License: GPLv3
#


import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "site", nargs="?", help="site used in the password generation (required)", default=''
    )
    parser.add_argument(
        "login", nargs="?", help="login used in the password generation. Default to ''."
    )
    parser.add_argument(
        "master_password",
        default=os.environ.get("LESSPASS_MASTER_PASSWORD", None),
        nargs="?",
        help="master password used in password generation. Default to LESSPASS_MASTER_PASSWORD env variable or prompt.",
    )
    parser.add_argument(
        "-L",
        "--length",
        default=16,
        choices=range(5, 35 + 1),
        type=int,
        help="password length (default: 16, min: 5, max: 35)",
        metavar="[5-35]",
    )
    parser.add_argument(
        "-C", "--counter", default=1, type=int, help="password counter (default: 1)"
    )
    parser.add_argument(
        "--exclude",
        default=None,
        help="exclude char from generated password",
    )
    lowercase_group = parser.add_mutually_exclusive_group()
    lowercase_group.add_argument(
        "-l",
        "--lowercase",
        help="add lowercase in password",
        dest="l",
        action="store_true",
    )
    lowercase_group.add_argument(
        "--no-lowercase",
        help="remove lowercase from password",
        dest="nl",
        action="store_true",
    )

    uppercase_group = parser.add_mutually_exclusive_group()
    uppercase_group.add_argument(
        "-u",
        "--uppercase",
        dest="u",
        help="add uppercase in password",
        action="store_true",
    )
    uppercase_group.add_argument(
        "--no-uppercase",
        dest="nu",
        help="remove uppercase from password",
        action="store_true",
    )

    digits_group = parser.add_mutually_exclusive_group()
    digits_group.add_argument(
        "-d", "--digits", dest="d", help="add digits in password", action="store_true"
    )
    digits_group.add_argument(
        "--no-digits",
        dest="nd",
        help="remove digits from password",
        action="store_true",
    )

    symbols_group = parser.add_mutually_exclusive_group()
    symbols_group.add_argument(
        "-s", "--symbols", dest="s", help="add symbols in password", action="store_true"
    )
    symbols_group.add_argument(
        "--no-symbols",
        dest="ns",
        help="remove symbols from password",
        action="store_true",
    )
    parsed_args = parser.parse_args()
    return parsed_args
