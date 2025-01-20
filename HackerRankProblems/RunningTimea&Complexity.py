import math
def isPrime(n):
    if (n <= 1) or ((n%2 == 0) and (n!=2)):
        return "Not prime"
    if n == 2:
        return "Prime"
    
    sqrt_n = int(math.sqrt(n))
    for i in range(3, sqrt_n + 1):
        if n % i == 0:
            return "Not prime"

    return "Prime"
        
if __name__=="__main__":
    t = int(input())
    # print(math.sqrt(t))
    for _ in range(t):
        n = int(input())
        print(isPrime(n))

