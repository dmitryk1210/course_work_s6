
from letter import Letter


def alphabet(n):
    for character in range(n):
        yield Letter("abcdefghijklmonpqrstuvwxyz"[character])
