def isprime(n):
    if n==2:
        return 1
    else:
        for i in range(2,n):
            if n % i == 0:
                return 0
        return 1
    
n = int(input())
for i in range(2,n):
    flag = isprime(i)
    if flag == 1:
        print(i)