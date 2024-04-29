#!/usr/bin/env python3

""" Hash random values with a fixed difficulty
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
    """Hash random values and print any digests lower than the target
    difficulty
    """
    # Put your own initials here so you can personalise your blockchain!
    base = "CryptoSecEd Blockchain: "
    # The challenge variable has been set to an arbitrary value. To
    # have hashes of the desired type generated at a particular rate,
    # this value will need to be either increased or decreased.
    challenge = "000f"
    difficulty = challenge + "f"*(64-len(challenge))
    count = 0
    start = time.time()
    print(f"Difficulty: {difficulty}")

    while True:
        random_value = randint(1, 1000000000000)
        test_string = base + str(random_value)
        current_hash = gen_hash(test_string)
        if current_hash < difficulty:
            count = count + 1
            end = time.time()
            elapsed = end - start
            print(f"{test_string}, count: {count}, elapsed time: {elapsed} s")
            print(f"Hash: {current_hash}\n")


if __name__ == "__main__":
    main()
