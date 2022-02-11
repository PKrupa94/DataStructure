# types of recursion
# 1 Tail recursion
# 2 Head recursion
# 3 Tree recursion
# 4 Indirect recursion

# Tail recursion

def calculate_squre_rec_tail(n):
    if n > 0:
        k = n ** 2
        print('tail recursion', k)
        # In tail recursion there must be no statement after fun call
        calculate_squre_rec_tail(n-1)


calculate_squre_rec_tail(4)

# head


def calculate_squre_rec_head(n):
    if n > 0:
        # In head recursion there must be no statement between base condition and fun call
        calculate_squre_rec_head(n-1)
        k = n ** 2
        print('head recursion', k)


calculate_squre_rec_head(4)

# tree recursion
#  # In tree recursion fun call 2 times

#complexity = O(2^n)


def calculate_squre_rec_tree(n):
    if n > 0:
        calculate_squre_rec_tree(n-1)
        k = n ** 2
        print('tree recursion', k)
        calculate_squre_rec_tree(n-1)


calculate_squre_rec_tree(4)
