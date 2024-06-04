#
# Copyright (C) Stanislaw Adaszewski, 2024
# License: GPLv3
#


from .cli import *
from .profile import *
from .password import *
import tkinter.simpledialog
import getpass
import asyncio
import aioconsole as aioc
import os


async def wait_keypress_with_timeout(timeout=5):    
    t = asyncio.create_task(aioc.ainput())
    await asyncio.wait([ t ], timeout=timeout)


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


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
        root.destroy()
    except:
        master_password = getpass.getpass('Master Password: ')
    if master_password is None:
        print('Master password not provided. Aborting...')
        return
    password_profile = create_profile(args)
    password = generate_password(password_profile, master_password)
    try:
        import pyperclip
    except:
        print('Press ENTER to obtain the second half. First half of the password:')
        print(password[:len(password)//2])
        input()
        clear_screen()
        print('Press ENTER to clear the screen. Auto-clear in 10 seconds. Second half:')
        print(password[len(password)//2:])
        asyncio.run(wait_keypress_with_timeout(10))
        clear_screen()
        return
    pyperclip.copy(password[:len(password)//2])
    print('Half of the password copied to the clipboard. Press ENTER to get the second part copied to the clipboard')
    input()
    pyperclip.copy(password[len(password)//2:])
    print('Second half of the password copied to the clipboard. Press ENTER to clear the clipboard. Auto-clear in 10 seconds...')
    asyncio.run(wait_keypress_with_timeout(10))
    pyperclip.copy('')



if __name__ == '__main__':
    main()
