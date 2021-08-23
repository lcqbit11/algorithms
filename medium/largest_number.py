

def largest_number(nums):
    if not nums:
        return 
    
    n = len(nums)
    for i in range(n):
        for j in range(n-1-i):
            if str(nums[j])+str(nums[j+1]) < str(nums[j+1])+str(nums[j]):
                nums[j] = nums[j] + nums[j+1]
                nums[j+1] = nums[j] - nums[j+1]
                nums[j] = nums[j] - nums[j+1]

    res = ''
    res = '0' if nums[0] == 0 else ''.join(map(str, nums))
    return res


if __name__ == "__main__":
    nums = [3,30,34,5,9]
    res = largest_number(nums)
    print(res)