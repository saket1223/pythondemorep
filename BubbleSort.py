# Bubble sort

def sortDesc(list):
    for i in range(len(list) - 1, 0, -1):
        for j in range(i):
            if list[j] < list[j + 1]:
                temp = list[j + 1]
                list[j + 1] = list[j]
                list[j] = temp
    return list


def sortAsc(list):
    for i in range(len(list) - 1, 0, -1):
        for j in range(i):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    return list


list = [2, 4, 5, 1, 3]
print(sortAsc(list))
print(sortDesc(list))
