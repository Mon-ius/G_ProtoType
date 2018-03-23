a = [(1, 2), (4, 1), (9, 10), (13, -3)]
b = [(1, 2), (4, 1), (13, -3), (9, 10)]
data = zip(a, b)

list1, list2 = map(lambda t: list(t), zip(*data))

print(list1,list2)96

3=-