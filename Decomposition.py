from math import ceil, floor
import time

def Time_gap(q, start = 0):
    if q == 1:
        return time.time()
    if q == 2:
        print("time - ", "--- %s seconds ---" % (time.time() - start))



def Dec(n, q):
    s=0
    ss=0
    if q == 2:
        for i in range(1, n+1):
            for j in range(n):
                ss+=1
                if i>=j and i+j == n:
                    print (i, j)
                    s+=1
        print(s, ss)
    if q == 3:
        for i in range(1, n+1):
            for j in range(n):
                for k in range(n):
                    ss+=1
                    if i>=j>=k and i+j+k == n:
                        #print (i, j, k)
                        s+=1

    if q == 4:
        for i in range(1, n+1):
            for j in range(n):
                for k in range(n):
                    for t in range(n):
                        ss+=1
                        if i>=j>=k>=t and i+j+k+t == n:
                            #print (i, j, k, t)
                            s+=1
    if q == 5:
        for i in range(1, n+1):
            for j in range(n):
                for k in range(n):
                    for t in range(n):
                        for y in range(n):
                            ss+=1
                            if i>=j>=k>=t>=y and i+j+k+t+y == n:
                                print (i, j, k, t, y)
                                s+=1
    print(f'iteration: {s, ss}')


def Dec_(n):

    s = 0
    max_a = ceil(n/4) + 1
    max_b = ceil(n/3) + 1
    max_c = ceil(n/2) + 1

    for a in range(max_a):
        for b in range(a, max_b):
            for c in range(b, max_c):
                d = n - (a+b+c)
                if d >= c:
                    s += 1
                else:
                    break
                #print(a,b,c,d)
    print(s)

def Decomposition(n, q, l=0):
    """n - number, q - quantity of terms, l - limit, s - iterations"""

    count = 0
    
    if l == 0:
        l = n

    min_n = ceil(n/q)

    if q == 2:
        if l < n:
            return n - min_n - (n-l) + 1
        else:
            return n - min_n + 1
    else:
        max_limit = 0

        if l < n:
            max_n = l + 1
        else:
            max_n = n + 1

        for i in range(min_n, max_n):
            count += Decomposition(n-i, q-1, i)

        return count

num = 100
q = 3

start = Time_gap(1)

print(Decomposition(num, q))
Time_gap(2, start)

#start = Time_gap(1)
#Dec(num, q)
#Time_gap(2, start)

start = Time_gap(1)
Dec_(num)
Time_gap(2, start)
