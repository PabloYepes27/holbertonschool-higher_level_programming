#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for i in range(0, len(dir(hidden_4))):
        arguments = dir(hidden_4)[i]
        if (arguments[0] != '_'):
            print(arguments)
