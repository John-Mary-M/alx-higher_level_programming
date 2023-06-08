#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    num_args = len(args)

    if num_args == 0:
        print('{} arguments.'.format(num_args))
    else:
        print('{} arguement:'.format(num_args))
        for i, args in enumerate(args):
            print('{}: {}'.format(i+1, args))
