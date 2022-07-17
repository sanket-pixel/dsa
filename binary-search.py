def search(nums, target) :
    s = 0
    e = len(nums) - 1
    while (True):
        m = int((s + e) / 2)
        if s >= e:
            return -1
        if target < nums[m]:
            e = m - 1
        elif target > nums[m]:
            s = m + 1
        elif target == nums[m]:
            return m



idx = search([1,2,3,4,5],6)
