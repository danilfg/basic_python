a = [21, 54, 6.44, 6, 3, 2, 7675, 32442244, 3424]
print(a)
a.append(200)
a.append('200')
a.append(True)
a.append([True, False])
a.insert(1, 55)
a.append(True)

# print(a)

# a.remove(True)
# a.remove(True)
# a.remove(True)

# last_el = a.pop()
# print(a)
# print(last_el)

index_el = a.pop(3)
# print(a)
# print(index_el)

# a.clear()
# print(a)

# b = a[:]
# b = list(a)
b = a.copy()
# print(id(a))
# print(id(b))

# print(a)
# # print(a.count('123'))
# # print(a.index(True, 12))
# a.reverse()
# print(a)
c = [21, 55, 54, 6, 3, 2, 7675, 32442244, 3424, 200]
c.sort(reverse=True)
print(c)

d = sorted(c)
print(d)
