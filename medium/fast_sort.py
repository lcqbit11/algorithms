
def fast_sort(nums, low, high):
    if low >= high:
        return 
    
    pilot = nums[low]
    start, end = low, high
    while start < end:
        while start < end and nums[end] >= pilot:
            end -= 1
        while start < end and nums[start] <= pilot:
            start += 1
        if start < end:
            nums[start], nums[end] = nums[end], nums[start]
    nums[low] = nums[start]
    nums[start] = pilot

    fast_sort(nums, low, start - 1)
    fast_sort(nums, start + 1, high)


if __name__ == "__main__":
    nums = [9, 3, 6, 2, 7, 1, 2]
    fast_sort(nums, 0, len(nums) - 1)
    res = ''
    for i in range(len(nums)):
        res += str(nums[i]) + ' '
    print(res)
            
