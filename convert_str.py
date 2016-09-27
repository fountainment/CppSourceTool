#!/usr/bin/env python

import sys

def main():
    argn = len(sys.argv)
    if argn != 2:
        print 'usage: convert_str.py [FileName]'
        return

    f = open(sys.argv[1], 'r')
    lines = f.readlines()
    n = len(lines)
    for i in xrange(n):
        lines[i] = lines[i].rstrip()
        lines[i] = '"%s\\n"' % lines[i]
	print lines[i]

if __name__ == '__main__':
    main()
