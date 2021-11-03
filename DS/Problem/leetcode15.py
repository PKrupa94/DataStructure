# three sum
def threeSum(self, nums):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i-1] != nums[i]:
            twosum(nums[i+1:len(nums)], nums[i], result)
    return result


def twosum(arr, num, result):
    i = 0
    j = len(arr) - 1
    while i < j:
        total = arr[i] + arr[j] + num
        if total < 0:
            i += 1
        elif total > 0:
            j -= 1
        else:
            result.append([num, arr[i], arr[j]])
            i += 1
            j -= 1
            while i < j and arr[i-1] == arr[i]:
                i += 1
    return result
