#!/usr/bin/env python
"""taken and modified from https://gist.github.com/rji/b38c7238128edf53a181"""
import hashlib
import sys


def sha256_checksum(filename, block_size=65536):
    """sha256 checksum."""
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            sha256.update(block)
    return sha256.hexdigest()


def main():
    """main func."""
    for f in sys.argv[1:]:
        checksum = sha256_checksum(f)
        print(f + '\t' + checksum)


if __name__ == '__main__':
    main()
