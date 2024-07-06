#!/usr/bin/python3

"""Adrgnjaner hretj ertu skeert hr t gnvlajlb ert  reth nsg"""
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    data = parse.urlencode(value).encode("ascii")

    request = request.Request(url, data)
    with request.urlopen(request) as resp:
        print(resp.read().decode("utf-8"))
