"""Extracts the private key as hex string from a Geth keyfile."""

import getpass
import sys
import os

import web3

w3 = web3.Web3()

if __name__ == "__main__":
    if len(sys.argv) < 2 or not os.path.isfile(sys.argv[1]):
        print("Usage: extract-private-key <keyfile>", file=sys.stderr)
        sys.exit(1)

    with open(sys.argv[1], encoding="utf-8") as keyfile:
        encrypted_key = keyfile.read()

    pwd = getpass.getpass("Keyfile password: ")
    key = w3.eth.account.decrypt(encrypted_key, pwd)
    print(key.hex())
