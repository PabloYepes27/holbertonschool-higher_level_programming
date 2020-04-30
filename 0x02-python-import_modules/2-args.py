#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if (len(sys.argv) == 1):
        ar = "arguments."
    elif (len(sys.argv) == 2):
        ar = "argument:"
    else:
        ar = "arguments:"
    print("{} {}".format(len(sys.argv) - 1, ar))
    for i in range(1, len(sys.argv)):
        arguments = sys.argv[i]
        print("{}: {}".format(i, arguments))
