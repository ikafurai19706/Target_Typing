# coding: utf-8
import hashlib
with open('1400-test.txt', 'rb') as checksum:
    print(hashlib.sha256(checksum.read()).hexdigest())
