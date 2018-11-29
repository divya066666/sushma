def countOccurrences (N, K): 
    n = len(N) 
    c1 = 0
    c2 = 0
    C = 0
    for i in range(n): 
        if N[i] == 'a': 
            c1+= 1 
            if N[i] == 'b': 
              c2+= 1 
              C += c1
    return C * K + (K * (K - 1) / 2) * c1 * c2
N=43
k = 1233
print (countOccurrences(N, k)) 
  
