def sum(N):
    if N==0:
        return 0
    if N>0 :
        return N+sum(N-1)
print(sum(10))
        
    
        