N = 5

# result = []
# for num in range(1, N + 1):
#     result.append(num ** 2)

# result = [num ** 2 for num in range(1, N + 1)]
# print(result)

# numbers = [34, 63, 53, 93, 1, 0, 31]
# result_numbers = [num > 35 for num in numbers]
# print(result_numbers)

# numbers = [34, 63, 53, 93, 1, 0, 31]
# result_numbers = [num for num in numbers if num > 35 or num == 0]
# # result = []
# # for num in numbers:
# #     if num > 35:
# #         result.append(num ** 2)
#
# print(result_numbers)

# numbers = [-1, 3, 5, -4, 0, 12, -921]
# # result = []
# # for num in numbers:
# #     if num >= 0:
# #         result.append(f"{num} - положительное")
# #     else:
# #         result.append(f"{num} - отрицательное")
# # print(result)
#
# result = [f"{num} - положительное" if num >= 0 else f"{num} - отрицательное" for num in numbers]
# print(result)

# table_multply = [
#     f"{x} * {y} = {x  * y}"
#     for x in range(1, 10)
#     for y in range(1, 10)
# ]
table_multply = []
for x in range(1, 10):
    for y in range(1, 10):
        table_multply.append(f"{x} * {y} = {x * y}")

print(table_multply)
