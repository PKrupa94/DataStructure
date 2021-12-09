def threeSumClosest(nums, target):
    nums.sort()
    diff = float('inf')
    for i in range(len(nums)):
        low = i + 1
        high = len(nums)-1
        while low < high:
            total = nums[i]+nums[low]+nums[high]
            if abs(target-total) < abs(diff):
                diff = target - total
            if total < target:
                low += 1
            else:
                high -= 1
            if diff == 0:
                break
    return target - diff
