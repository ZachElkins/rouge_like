#!/usr/bin/env python3
from lib import *

def main():
    print("hello world")
    level = Level(10)
    print(np.matrix(level.get_map()))

if __name__ == '__main__':
    main()