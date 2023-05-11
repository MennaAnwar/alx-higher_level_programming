#!/usr/bin/python3
def add_arg(argv):
    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))

if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
