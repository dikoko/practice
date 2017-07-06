# 1-03. GCD
# Given a, b. Find the GCD (Greatest Common Divisor) of them.
# Please give both recursive and iterative solutions.

# by Euclidean algorithm
# recursive solution
def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

# iterative solution
def gcd_iter(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    
    while b > 0:
        a = a % b
        a,b = b,a
        
    return a
    

if __name__ == '__main__':
    print(gcd(117,13))
    print(gcd_iter(117,13))
