#
# Copyright (C) lesspass project
# License: GPLv3
#


def create_profile(args):
    profile = {
        "lowercase": False if args.nl else True,
        "uppercase": False if args.nu else True,
        "digits": False if args.nd else True,
        "symbols": False if args.ns else True,
        "length": args.length,
        "counter": args.counter,
        "site": args.site,
        "login": args.login or "",
        "exclude": args.exclude or "",
        "use_random_salt": False if args.no_random_salt else True,
        "use_scrypt": False if args.use_pbkdf2 else True,
        "regenerate_random_salt": True if args.regenerate_random_salt else False,
    }
    if args.l or args.u or args.d or args.s:
        profile["lowercase"] = args.l
        profile["uppercase"] = args.u
        profile["digits"] = args.d
        profile["symbols"] = args.s
    return profile
