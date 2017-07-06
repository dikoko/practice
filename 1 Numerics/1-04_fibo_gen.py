# 1-04. Fibonacci Generator
# Given N, find all fibonacci numbers equal or less than N

def fibo_gen(N):
    if N < 0: return []
    
    def _gen_fibo(n):
        prev_prev = 0
        prev = 1
        fibo = 1 
        while fibo <= n:
            yield fibo
            prev_prev = prev
            prev = fibo
            fibo = prev + prev_prev
    
    return [f for f in _gen_fibo(N)] 

if __name__ == '__main__':
    N = 100    
    print(fibo_gen(N))
