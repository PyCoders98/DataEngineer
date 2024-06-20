l1 = [1, 2312, 3, 41, 2, 6, 6, 45, 5, 4, 31, 3, 21, 36, 75]


def third_largest_element(lst):
    count = 0
    l2 = []
    l3 = []

    var = lst[0]
    for i in range(len(lst)):
        count += 1
        for j in range(0, len(lst)):
            if lst[i] < lst[j]:
                var = lst[j]
        l2.append(var)
        if count == 3:
            return l2


print(third_largest_element(l1))
