#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    resul = 0

    for i, arg in enumerate(sys.argv):
        if (i > 0):
            resul += int(arg)

    print(resul)
