# iteration

def calculate_squre_itr(n):
    while n > 0: # complexity n + 1
        k = n ** 2 # 1
        print('Squre using itr',k) #1
        n -= 1 #1
        # O(n+1) = O(n)


calculate_squre_itr(4)

#using recurion

def calculate_squre_rec(n):
    if n > 0:
        s = n**2
        print('Squre using rec',s)
        calculate_squre_rec(n-1)

calculate_squre_rec(4)