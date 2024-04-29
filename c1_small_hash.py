#!/usr/bin/env python3

""" Find a sequence of inputs that hash to successively smaller digests
"""

from hashlib import sha256
from random import randint

import time


def gen_hash(string):
    """ Calculates a hash of a string
    """
    hasher = sha256()
    hasher.update(string.encode('utf-8'))
    return hasher.hexdigest()


def main():
    """ Keep searching for strings whose hashes are lower values than
    the previous. Uses random integers instead of floats and prints
    more information.
    """
    base = "Decreasing hashes: "
    current_hash = gen_hash(base + str(0))
    top = current_hash
    count = 0
    start = time.time()

    # This next line is generally a bad idea. It will run forever
    # (or until you press CTRL-C)
    while True:
        random_value = randint(1, 1000000000000)
        test_string = base + str(random_value)
        current_hash = gen_hash(test_string)
        if current_hash < top:
            count = count + 1
            end = time.time()
            elapsed = end - start
            print(f"{test_string}, count: {count}, elapsed time: {elapsed}  s")
            print(f"Smallest hash: {current_hash}\n")
            top = current_hash


if __name__ == "__main__":
    main()
