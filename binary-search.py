# def search(nums, target) :
#     s = 0
#     e = len(nums) - 1
#     while (True):
#         m = int((s + e) / 2)
#         if s >= e:
#             return -1
#         if target < nums[m]:
#             e = m - 1
#         elif target > nums[m]:
#             s = m + 1
#         elif target == nums[m]:
#             return m






























def ceiling(nums, target):
    s = 0
    e = len(nums)-1
    if nums[-1] < target:
        return -1
    while(s<=e):
        m = int((s+e)/2)
        if nums[m] < target:
            s = m+1
        elif nums[m] > target:
            e = m -1
        elif nums[m] == target:
            return nums[m]
    if s>e :
        return  nums[s]

def sqrt(x):
    arr = []
    for i in range(x):
        arr.append(i)
    s = 0
    e = len(arr) - 1
    while (s <= e):
        m = int((s + e) / 2)
        if arr[m] * arr[m] < x:
            s = m + 1
        elif arr[m] * arr[m] > x:
            e = m - 1
        elif arr[m] * arr[m] == x:
            return arr[m]
    if (s > e):
        return arr[e]



#
c = ceiling([1,2,3,8,11],0)
print(c)