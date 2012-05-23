#!/usr/bin/env python

import time
import sys

CHAR_ON = u'\u25cf'
CHAR_OFF = u'\u25cb'

def binary_display(hour, minute, second):
    def bin_rep(s):
        ret = list()
        for x in xrange(4):
            ret.append(CHAR_ON if s % 2 else CHAR_OFF)
            s >>= 1
        return ret

    matrix = list()
    matrix.append(bin_rep(hour / 10))
    matrix.append(bin_rep(hour % 10))
    matrix.append(bin_rep(minute / 10))
    matrix.append(bin_rep(minute % 10))
    matrix.append(bin_rep(second / 10))
    matrix.append(bin_rep(second % 10))
    
    for x in xrange(3, -1, -1):
        for y in xrange(6):
            sys.stdout.write(matrix[y][x] + ' ')
        sys.stdout.write('\n')

def main():
    while True:
        t = time.localtime() 
        binary_display(t.tm_hour % 12, t.tm_min, t.tm_sec)
        time.sleep(1)
        sys.stdout.write('\x1b[1A\x1b[2K' * 4)

if __name__ == '__main__':
    main()  
