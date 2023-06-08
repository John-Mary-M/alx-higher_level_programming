#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_sum = sum(int(sys.argv[i]) for i in range(1, len(sys.argv)))
    print("{}".format(args_sum))
