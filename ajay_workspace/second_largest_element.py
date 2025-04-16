lst = [
    45,
    36,
    465,
    867,
    9,
    67,
    76,
    344,
    13,
    87989,
    4,
    52,
    4,
    3123,
]


def second_largest_element(l):
    v1 = l[0]
    temp = v1
    for i in range(len(lst)):
        if lst[i] > v1:
            temp = v1
            v1 = lst[i]

    return temp


print(second_largest_element(lst))
