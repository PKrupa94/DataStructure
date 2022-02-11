def sum_rec(n):
    if n == 0:
        return 0
    return sum_rec(n-1) + n


number = int(input('Enter Integer Number:'))
print(sum_rec(number))

#complexity : O(n)
