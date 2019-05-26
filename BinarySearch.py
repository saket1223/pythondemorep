# Binary Search required sorted list

pos = -1


def search(list, n):
    l = 0
    u = len(list) - 1
    while l <= u:
        mid = (l + u) // 2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False


list = [2, 3, 5, 1, 4, 7]
n = 2
sortedList = sorted(list)
if search(sortedList, n):
    print('found at position ', pos + 1)
else:
    print('Not fount in the list.')
