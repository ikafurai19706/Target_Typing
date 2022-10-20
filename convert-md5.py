# coding: utf-8
import hashlib
with open('1400-test.txt', 'r') as checksum:
    print(hashlib.md5(checksum.read()).hexdigest())
