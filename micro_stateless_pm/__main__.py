#
# Copyright (C) Stanislaw Adaszewski, 2024
# License: GPLv3
#


from .cli import *
from .profile import *
from .password import *
import getpass


def main():
    args = parse_args()
    master_password = getpass.getpass('Master Password: ')
    password_profile = create_profile(args)
    password = generate_password(password_profile, master_password)
    print(password)


if __name__ == '__main__':
    main()
