import os


def get_computer_name():
    return os.popen("whoami").read()
