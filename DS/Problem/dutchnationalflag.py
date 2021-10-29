
def dutch_flag_sort(balls):
    low, mid, high = 0, 0, len(balls)-1
    while mid <= high:
        pivot = balls[mid]
        if pivot == "R":
            balls[low], balls[mid] = balls[mid], balls[low]
            low += 1
            mid += 1
        elif pivot == "G":
            mid += 1
        else:
            balls[mid], balls[high] = balls[high], balls[mid]
            high -= 1
    return balls


print(dutch_flag_sort(["G", "B", "G", "G", "R", "B", "R", "G"]))
# Output: [R, R, G, G, G, G, B, B]
