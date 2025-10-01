# num: int = 0
#
#
# # num = '1.2'
#
# def plus_two(a: int | float, b: int | float) -> int | float:
#     return a + b
#
# res = plus_two(2.4, 4)
# #
# # print(plus_two(2, 4))
#
# print(plus_two.__annotations__)
#
# nums: list[int] = [2, 1, 3, 4, 5, 6]
#
# nums.append(2.4)
#
# print(nums)

# books = []
# book: tuple[str, str, int]
# book = ("Булгаков", 'Мастер и Маргарита', 1900)
# books.append(book)
# book = ("Булгаков", 'Мастер и Маргарита', '1900')

# capitals: dict[str, str] = {'Россия': 'Москва'}
# capitals['США'] = 922

def list_upper_case(lst: list[str]) -> list[str]:
    return [x.upper() for x in lst]


print(list_upper_case(['dwqd', 'grthtg', 2]))