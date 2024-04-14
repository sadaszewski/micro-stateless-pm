#
# Copyright (C) Stanislaw Adaszewski, 2024
# License: GPLv3
#


from .cli import *
from .profile import *
from .password import *
import tkinter.simpledialog
import getpass


def main():
    args = parse_args()
    root = None
    try:
        import hdpitkinter as tk
        root = tk.HdpiTk()
    except:
        try:
            import tkinter as tk
            root = tk.Tk()
        except:
            pass
    try:
        root.tk.eval(f'tk::PlaceWindow {root._w} center')
        master_password = tkinter.simpledialog.askstring("Password", "Enter password:", show='*', parent=root)
    except:
        master_password = getpass.getpass('Master Password: ')
    password_profile = create_profile(args)
    password = generate_password(password_profile, master_password)
    print(password)


if __name__ == '__main__':
    main()
