#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        res = ""
        if (i % 3 == 0):  # test multiples of 3
            res += "Fizz"
        if (i % 5 == 0):  # test multiples of 5
            res += "Buzz"
        print("{}".format(res) or "{}".format(i), end='')
        print(" ", end='')
