import sys
from time import perf_counter

"""
Cache function to store results from previous recursion
"""
cache = {}
def cacheFunc(func):
    def runner(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return runner

def weightOn(r, c):
    if r == 0:
        val = 0
    elif r == 1:
        val = 100
    else:
        if c == 0:
            lshoulder = 0
        else:
            lshoulder = (weightOn(r-1,c-1) + 200)/2
        if c == r:
            rshoulder = 0
        else:
            rshoulder = (weightOn(r-1, c) + 200)/2
        val = rshoulder + lshoulder
    return val


@cacheFunc
def main(a):
    start = perf_counter()
    for i in range(0, a):
        lst = []
        for l in range(0,i+1):
            lst.append(format(weightOn(i, l),'.2f'))
        print(" " * (15-len(lst)),lst)
    stop = perf_counter()
    runtime = (stop - start)
    print("Elapsed time:", runtime, "seconds")

if __name__ == "__main__":
    try:
        a = int(sys.argv[1])
        main(a)
    except IndexError:
        a = int(input("How many rows should we build?"))
        main(a) 
