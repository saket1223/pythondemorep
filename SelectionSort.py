# Selection Sort


def sort(nums):

    for i in range(len(nums) - 1):
        minpos = i
        for j in range(i, len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp


def sortDesc(nums):
    for i in range(len(nums) - 1):
        minpos = i
        for j in range(i, len(nums)):
            if nums[j] > nums[minpos]:
                minpos = j
        temp = nums[minpos]
        nums[minpos] = nums[i]
        nums[i] = temp


nums = [2, 4, 3, 1, 45, 5]
sort(nums)
print('Selection Sorted list:Ascending Order :',nums )
sortDesc(nums)
print('Selection Sorted list:Descending Order :', nums)
