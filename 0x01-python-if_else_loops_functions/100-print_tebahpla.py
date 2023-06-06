#!/usr/bin/python3
for i in range(ord('Z'), ord('A') - 1, -1):
    print(chr(i + 32 if i % 2 == 1 else i), end='')
