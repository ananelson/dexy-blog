# isprime() function taken from 
# http://www.daniweb.com/forums/post319401.html#post319401

### @export "is-prime"
def isprime(n):
    '''check if integer n is a prime'''
    # range starts with 2 and only needs to go up the squareroot of n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

### @export "2011-is-prime"
isprime(2011)

### @export "primes-to-sum"
PRIMES_TO_SUM = [157,163,167,173,179,181,191,193,197,199,211]
sum(PRIMES_TO_SUM)

### @export "check-all-prime"
[isprime(p) for p in PRIMES_TO_SUM]

### @export "check-consecutive"
for x in range(min(PRIMES_TO_SUM), max(PRIMES_TO_SUM)+1):
    if isprime(x):
        if x in PRIMES_TO_SUM:
            print "%s is prime and already in PRIMES_TO_SUM" % x
        else:
            raise Exception("%s is prime and not in PRIMES_TO_SUM" % x)
    else:
        print "%s is not prime" % x

### @export "assertions"
assert isprime(2011)
assert all([isprime(p) for p in PRIMES_TO_SUM])
assert sum(PRIMES_TO_SUM) == 2011
