import random


# x = random.random() # от 0.0 до 1.0 не включительно
# print(x)

random.seed(123)
x = random.uniform(1, 10)
print(x)
y = random.uniform(1, 10)
print(y)
#
# x = random.randint(1, 10)
# print(x)

# x = random.randrange(1, 10, 2)
# print(x)

# nums = [2, 1, 3, 4, 5, 6]
#
# x = random.choice(nums)
# print(x)