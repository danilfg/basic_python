a = 18
b = 15

if a > b:
    res = a
else:
    res = b

print(res)

res = print(a + 10) if a > b else b
print("запринтовали res второй раз", res)