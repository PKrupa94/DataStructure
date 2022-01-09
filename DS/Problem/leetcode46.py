from _typeshed import Self


result = []


def permute(nums):
    helper(nums, 0, [])
    global result
    return result


def helper(nums, i, slate):
    if i == len(nums):
        global result
        result.append(slate[:])
    else:
        for pick in range(i, len(nums)):
            nums[pick], nums[i] = nums[i], nums[pick]
            slate.append(nums[i])
            helper(nums, i+1, slate)
            slate.pop()
            nums[pick], nums[i] = nums[i], nums[pick]

# alternate approach


result1 = []


def permute1(nums):
    helper1(nums, 0, [])
    global result1
    return result1


def helper1(nums, slate):
    if len(nums) == 0:
        global result1
        result1.append(slate)
    else:
        for i in range(len(nums)):
            helper1(nums[:i]+nums[i+1:], slate+[nums[i]])
