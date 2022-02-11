def factorial_Rec(n):
    if n == 0:
        return 1

    return factorial_Rec(n-1) * n


number = int(input('Enter Integer Number:'))
print(factorial_Rec(number))

#complexity : O(n)
