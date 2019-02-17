import time
import random
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
random.seed(time.time())

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
    divs += nprimes[len(nprimes) - 1]
    nprimes.pop(len(nprimes) - 1)
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

def task1makeplot():
    n = random.randint(1000,2500)
    fig, ax = plt.subplots()
    ax.scatter(n, 3*n,c = 'r',s = None, alpha = .7,label = "Euclidean Algorithm")
    ax.scatter(n, 3 * n, c='g', s=None, alpha=.7, label= "Consecutive Integer Checking")
    ax.grid(False)
    fig.tight_layout()
    title = "GCD Algorithms & Divisions from N=0 to N=" + str(n)
    ax.set_title(title)
    ax.set_ylabel("# of Divisions")
    ax.set_xlabel("Value approaching N")
    ax.axis([0,n,0,n])
    ax.legend(loc = 'upper right')

    divlist1 = []
    divlist2 = []
    for i in range(0,n):
        pack1 = gcd(i, n)
        pack2 = consecgcd(i, n)
        ax.plot(i ,pack1[0],'ro',label = "Euclidean Algorithm",markersize=5,alpha=.7)
        ax.plot(i, pack2[0], 'go', label="Consecutive Integer Checking Algorithm",markersize=5,alpha=.7)
        divlist1.append(pack1[0])
        divlist2.append(pack2[0])


    plt.show()

def task2makeplot(mode):
    k = random.randint(500, 1000)
    f = getfib(k + 1)

    title = "Euclids Algorithm Worst Case # of Divisions"
    fig,ex = plt.subplots()
    ex.scatter(f[k], f[k], c=None, s=None, alpha=.7)
    ex.grid(False)
    ex.set_title(title)
    ex.axis([0,k,0,k*3])
    ex.set_ylabel("# of divisions")
    ex.set_xlabel("Digit of Fibonacci Sequence")
    if mode == 0:
        ex.set_ylabel("Time Elapsed in nanoseconds.")
        ex.axis([0,k,0,1])
    for i in range(1,k):
        then = time.process_time()
        pack = gcd(f[k-i], f[k - i - 1])
        if mode == 1:
            ex.plot(k-i,pack[0],'ro',markersize=3)
        else:
            now = time.process_time()
            print("Operation clocked at:" ,now)
            ex.plot(k-i,now,'ro',markersize = 5)


    plt.show()

def task3makeplot():
    u = 3000
    title = "Middle School Method Complexity"
    fix,mx = plt.subplots()
    mx.set_title(title)
    mx.scatter(u, u, c=None, s=None, alpha=.7)
    mx.set_ylabel("# of divisions")
    mx.set_xlabel("Value of M")
    mx.axis([0,u,0,u])
    for i in range(2000):
        m = random.randint(0,u)
        n = random.randint(0,m)
        unpack = middleschool(m,n)
        mx.plot(m,unpack[1], 'bo',markersize = 5)

    plt.show()
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
fibonacci sequence on Euclid's algorithm.\n3: Input M and N, program outputs GCD(m,n) using the 'middle-school' method.")
        task = input()

        if task == "1":
            divlist1 = []
            divlist2 = []
            n = int(input("Input N: "))
            for i in range(n):
                pack1 = gcd(i, n)
                pack2 = consecgcd(i, n)
                divlist1.append(pack1[0])
                divlist2.append(pack2[0])

            divtotal1 = 0
            divtotal2 = 0
            for divs in divlist1:
                divtotal1+=divs

            for divs in divlist2:
                divtotal2+=divs



            print("Average # of divisions for Euclids Algorithm(MDavg(n)):", divtotal1/len(divlist1))
            print("Average # of divisions for Consecutive Integer Checking Algorithm(Davg(n)):", divtotal2/len(divlist2))




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
        inp = input("Which scatter plot would you like to view?\n1. Task 1, the difference between Consecutive Integer"
                    + " Checking and Euclid's Algorithm\n2. Task 2, worst case performance of Euclid's Algorithm\n"
                    + "3. Task 3, demonstration of linear complexity of middle-school method.\n")

        if inp == "1":
            task1makeplot()
        elif inp == "2":
            task2makeplot(1)
        elif inp == "3":
            task3makeplot()

    else:
        print("Invalid Entry.")





main()