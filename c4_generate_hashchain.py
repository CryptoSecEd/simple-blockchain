#!/usr/bin/env python3

"""Generate a log of input messages and protect them with a hashchain
"""

from hashlib import sha256


def gen_hash(string):
    """ Calculates a hash of a string
    """
    hasher = sha256()
    hasher.update(string.encode('utf-8'))
    return hasher.hexdigest()


def main():
    """Request lines of input text and write to the log with chained
    hashes
    """
    logfile = "log.txt"
    print("Welcome to the secure chat terminal.")
    print("All text will be entered into a verifiably secure ledger!")
    print("Enter N/n to quit")
    with open(logfile, "w+", encoding="utf-8") as write_first:
        write_first.write("f"*64 + " - Welcome to the secure chat terminal.\n")

    response = input()

    while response.lower() != "n":
        line = ""
        with open(logfile, "r", encoding="utf-8") as read_last:
            # We need to skip to the last line of the log file
            for line in read_last:
                pass
        with open(logfile, "a", encoding="utf-8") as append:
            append.write(gen_hash(line) + " - " + response + "\n")
        response = input()


# This is common in python code, and can be ignored for now
if __name__ == "__main__":
    main()
