import sys

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def print_even(n):
    print ' '.join(str(x) for x in xrange(int(n)) if is_even(x))

print_even(sys.argv[1])
