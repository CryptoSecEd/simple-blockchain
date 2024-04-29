#!/usr/bin/env python3

"""When started, the miner is asked to enter their name. Blocks are
generated and appended to a file (which checks for competing miners)
"""

from hashlib import sha256
from pathlib import Path
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


def verify_blockchain(blockchain_file, genesis, difficulty):
    """Reads the blockchain file and verifies it. If there is an error,
    it throws and exception. If it is valid, it returns the hash of the
    last line.
    """
    bc_file = Path(blockchain_file)
    if bc_file.is_file():
        with open(bc_file, 'r', encoding="utf-8") as read_bc:
            # The first hash in the blockchain cannot be checked
            # (since there is no previous hash)
            block_line = read_bc.readline().rstrip('\n')
            prev_hash = read_bc.readline().rstrip('\n')
            for block_line in read_bc:
                block_line = block_line.rstrip('\n')
                block = prev_hash + '\n' + block_line + '\n'
                cur_hash = gen_hash(block)
                block_file_hash = read_bc.readline().rstrip('\n')
                if cur_hash != block_file_hash:
                    print("Hashchain broken!")
                    print(f"Hash from file: {block_file_hash}")
                    print(f"Calculated hash: {cur_hash}")
                    raise ValueError("Hashchain broken")
                if block_file_hash > difficulty:
                    print("Hash is above difficulty!")
                    raise ValueError("Hash is above difficulty")
                prev_hash = cur_hash
    else:
        prev_hash = "f"*64
        with open(bc_file, 'w', encoding="utf-8") as write_bc:
            write_bc.write(genesis + '\n')
            write_bc.write(prev_hash + '\n')
    print("Blockchain verified!")
    return prev_hash


def main():
    """Search for new blocks and append them to the file when found.
    """
    bc_file = "blockchain.txt"
    challenge = "00000e"
    difficulty = challenge + "f"*(64-len(challenge))
    miner = input("Please enter your name: ")
    # Put your own name here so you can personalise your blockchain!
    base = "CryptoSecEd Blockchain"
    base = base + " Miner:" + miner + " "
    prev_hash = verify_blockchain(bc_file,
                                  "CryptoSecEd Blockchain: Genesis block",
                                  difficulty)

    count = 0
    start = time.time()
    print(f"Difficulty: {difficulty}\n")
    addresses = set(["alice", "bob", "chloe", "david", "elaine"])
    block_contents = base + random_tx(addresses)

    while True:
        random_value = randint(1, 1000000000000)
        test_string = block_contents + " Nonce: " + str(random_value) + "\n"
        cur_hash = gen_hash(prev_hash + "\n" + test_string)
        if cur_hash < difficulty:
            latest_hash = verify_blockchain(bc_file,
                                            "CryptoSecEd Blockchain: Genesis" +
                                            " block",
                                            difficulty)
            if prev_hash != latest_hash:
                print("Beaten by another miner, block discarded!")
                prev_hash = latest_hash
            else:
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
