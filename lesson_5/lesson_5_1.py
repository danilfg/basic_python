# streets = ['Ломоносова', 'Ленина', 'Артюхиной']
# ages = [23, 54, 26]

"""
        0           1           2
 ['Ломоносова', 'Ленина', 'Артюхиной']
        -3          -2          -1
"""
# print(streets[-2])
# print(streets[2])
# print(streets[-1])

# print(streets[3])
#
# avg_age = int(sum(ages) / len(ages))
# print(avg_age)

# ages[1] = 31
#
# print(ages)

# lst = ['Волгоград', 332, 21.232, True, False, [2, 3, 4, 'ывцй']]
lst = []
lst2 = list()
lst3 = list('Волгоград')
# print(len(lst3))
# print(max(ages))
# print(min(ages))
# print(sum(ages))
# print(sorted(lst3))
# print(sorted(ages))
# print(sorted(ages, reverse=True))

# print(sum(lst3))


streets = ['Ломоносова', 'Ленина', 'Артюхиной']
ages = [23, 54, 26]

result = streets + ages

# print(result +['А'] )
# print(result * 2)
# print('Ломоносова' in result)
# print('монос' in result)
# print(54 in result)

result.append('1212')
result.append([2, 5])
print(result)

del result[-1]
del result[1]
del result[1]

print(result)

