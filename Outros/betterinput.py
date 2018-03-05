# AUTOR: BRUNO GODOI MACHADO

import builtins


def int(text):
    try:
        return builtins.int(input(text))
    except ValueError:
        return int(text)


def float(text):
    try:
        return builtins.float(input(text))
    except ValueError:
        return float(text)


def bool(text):
    try:
        return builtins.bool(input(text))
    except ValueError:
        return bool(text)