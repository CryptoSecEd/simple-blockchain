#!/usr/bin/env python3

"""Verify the hash chain in a log file
"""

from hashlib import sha256


def gen_hash(string):
    """ Calculates a hash of a string
    """
    hasher = sha256()
    hasher.update(string.encode('utf-8'))
    return hasher.hexdigest()


def main():
    """Open the log file and verify each hashchain
    """
    logfile = "log.txt"
    print("We will now verify the authenticity of the log file.")
    first = True
    intact = True
    with open(logfile, encoding="utf-8") as read_log:
        for line in read_log:
            if first:
                first = False
                last_line = line
            else:
                split_line = line.split(" - ", 1)
                current_hash = split_line[0]
                if gen_hash(last_line) != current_hash:
                    print("The hashchain in the log file is not correct")
                    print(last_line)
                    print(f"Hash of previous line is: {gen_hash(last_line)}")
                    print(f"Corresponding hash from log: {current_hash}")
                    intact = False
                last_line = line
    if intact:
        print("The log file is intact. No unauthorised changes have been made.")
    else:
        print("The log file has been modified.")


if __name__ == "__main__":
    main()
