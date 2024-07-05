#!/usr/bin/python3

"""Adrgnjaner hretj ertu skeert hr t gnvlajlb ert  reth nsg"""
from urllib import request
from sys import argv


if __name__ == "__main__":
    with request.urlopen(argv[1]) as resp:
        print(dict(resp.headers).get("X-Request-Id"))
