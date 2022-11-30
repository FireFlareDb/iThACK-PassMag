import sys

from iThACK.manage import select_account, add_account, delete_account


def process(argv, argc):
    if argc == 0:
        select_account()
        sys.exit(0)

    if argv[0] == "add":
        add_account()
    elif argv[0] == "delete":
        delete_account()