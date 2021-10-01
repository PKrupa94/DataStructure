# select one element at time from the left of the list
# insert that element at its proper position
# after insertion every element to its left will be sorted

def insertion_sort(arr):
    for i in range(1, len(arr)):
        # this value needs to insert at pertivcular index
        current_value = arr[i]
        current_index = i
        while current_index > 0 and arr[current_index - 1] > current_value:
            arr[current_index] = arr[current_index - 1]
            current_index -= 1
        arr[current_index] = current_value
    return arr


arr = [3, 5, 8, 9, 6, 2]
print('insertion sort', insertion_sort(arr))
