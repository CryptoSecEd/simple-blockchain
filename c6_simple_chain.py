#!/usr/bin/env python3

"""This code starts to mine the blockchain from scratch, and appends
each new block to a text file
"""

from hashlib import sha256
from random import randint, sample

import time


def gen_hash(string):
    """ Calculates a hash of a string
    """
    hasher = sha256()
    hasher.update(string.encode('utf-8'))
    return hasher.hexdigest()


def random_tx(addresses):
    """Pick two random entries from the list of addresses and return a
    transaction between
    """
    pair1 = sample(list(addresses), 2)

    return "payer: " + pair1[0] + " receiver: " + pair1[1] + " amount: " \
        + str(randint(1, 100))


def add_new_block(string, cur_hash, filename):
    """Append the string to the file
    """
    with open(filename, "a+", encoding="utf-8") as append_file:
        append_file.write(string)
        append_file.write(cur_hash + "\n")


def main():
    """Search for new blocks and append them to the file when found.
    """
    bc_file = "simple_blockchain.txt"
    prev_hash = "f"*64
    # Put your own name here so you can personalise your blockchain!
    base = "CryptoSecEd Blockchain: "
    add_new_block(base + "Genesis block\n", prev_hash, bc_file)

    count = 0
    start = time.time()
    challenge = "00000e"
    difficulty = challenge + "f"*(64-len(challenge))
    print(f"Difficulty: {difficulty}\n")
    addresses = set(["alice", "bob", "chloe", "david", "elaine"])
    block_contents = base + random_tx(addresses)

    while True:
        random_value = randint(1, 1000000000000)
        test_string = block_contents + " Nonce: " + str(random_value) + "\n"
        cur_hash = gen_hash(prev_hash + "\n" + test_string)
        if cur_hash < difficulty:
            count = count + 1
            end = time.time()
            elapsed = end - start
            print(test_string, end="")
            print(cur_hash)
            print(f"Count: {count} Elapsed time: {elapsed} sec")
            add_new_block(test_string, cur_hash, bc_file)
            prev_hash = cur_hash
            block_contents = base + random_tx(addresses)


# This is common in python code, and can be ignored for now
if __name__ == "__main__":
    main()
