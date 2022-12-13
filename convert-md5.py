# coding: utf-8
import hashlib
with open("1400.txt", "rb") as checksum:
	print(hashlib.md5(checksum.read()).hexdigest())
with open("1900.txt", "rb") as checksum:
	print(hashlib.md5(checksum.read()).hexdigest())