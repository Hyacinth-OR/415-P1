import math
from collections import Counter

def gcd(m, n):
    # Return the GCD of a and b using Euclid's Algorithm
    divs = 0  # Keeping track of ops
    pack = []
    while m != 0:
        m, n = n % m, m
        divs+=1
    pack.append(divs)
    pack.append(n)

    return pack

def getfib(n):
    pack = [0]
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
        pack.append(b)
    return pack

def consecgcd(m, n):
    pack = []
    divs= 0
    if m > n:
        min = n
    else:
        min = m

    while(min > 0):
        if(m % min == 0):
            divs+=2
            if (n % min == 0):
                pack.append(divs)
                pack.append(min)
                return pack
        else:
            divs+=1

        min = min-1
    pack.append(divs) # Pack[0] Is always the divisions done
    pack.append(m)  # Pack[1] Is the GCD
    return pack

def middleschool(m,n):
    mprimes = sieve(m)
    nprimes = sieve(n)
    divs = 0
    divs += mprimes[len(mprimes)-1]
    mprimes.pop(len(mprimes)-1)
    print(mprimes)
    divs += nprimes[len(nprimes) - 1]
    nprimes.pop(len(nprimes) - 1)
    print(nprimes)
    common = intersection(mprimes,nprimes)
    sum = 1
    for elem in common:
        sum = sum * elem
    pack = []
    pack.append(sum)
    pack.append(divs)
    return pack

def intersection(list1,list2):
    list3 = list((Counter(list1)& Counter(list2)).elements())
    return list3

def sieve(n):
    pack = []
    divs = 0
    i = 2
    while n > 1:
        divs+=1
        if n % i == 0:
            pack.append(i)
            n /= i
            divs+=1
        else:
            i += 1
    pack.append(divs) # at the end, we pop this when it's called in the middle school algorithm
    return pack

def main():
    print("Select mode:\n1: User Testing Mode\n2: Scatter plot Mode")
    mode = input()
    if mode == "1":
        print("Select task:\n1: Input N, Output MDavg(n) and Davg(n).\n2: Input K, Output GCD(m,n) using \
fibonacci sequence on Euclid's algorithm.\n3:Input M and N, program outputs GCD(m,n) using the 'middle-school' method.")
        task = input()
        if task == "1":
            m = int(input("Input M: "))
            n = int(input("Input N: "))
            pack1 = gcd(m, n)
            pack2 = consecgcd(m,n)
            gcrd1 = pack1[1]
            divs1 = pack1[0]
            gcrd2 = pack2[1]
            divs2 = pack2[0]

            print("GCD of ",m, " and ",n," is ",gcrd1)
            print("GCD calculated in ",divs1," divisions using Euclid's Algorithm.")
            print("GCD calculated in ", divs2, " divisions using Consecutive Integer Checking.")

        if task == "2":
            k = int(input("Input K: "))
            f = getfib(k+1)
            pack = gcd(f[k+1], f[k])
            gcrd = pack[1]
            divs = pack[0]
            print("GCD of ", f[k+1], " and ", f[k], " is ", gcrd)
            print("Worst Case GCD calculated in ", divs, " divisions.")
        if task == "3":
            m = int(input("Input M: "))
            n = int(input("Input N: "))
            unpack = middleschool(m,n)
            gcrd = unpack[0]
            divs = unpack[1]
            print("GCD of ",m, " and ",n," is ",gcrd,".")
            print("GCD calculated in ", divs, " divisions using middleschool method.")

    elif mode == "2":
        pass

    else:
        print("Invalid Entry.")





main()