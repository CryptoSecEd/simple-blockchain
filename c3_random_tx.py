#!/usr/bin/env python3

"""Generate random transactions for use in a blockchain
"""

from random import randint, sample


def random_tx(addresses):
    """Pick two random entries from the list of addresses and return a
    transaction between
    """
    pair1 = sample(list(addresses), 2)

    return "payer: " + pair1[0] + " receiver: " + pair1[1] + " amount: " \
        + str(randint(1, 100))


def main():
    """Define a set of names to be the addresses, then generate a random
    transaction between them
    """
    addresses = set(["alice", "bob", "chloe", "david", "elaine"])
    transaction = random_tx(addresses)
    print(transaction)


if __name__ == "__main__":
    main()
