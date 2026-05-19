def g(n):
    if n <= 1:
        return 1
    #print(n * g(n-1))
    return n * g(n-1)
    
print(g(5))

