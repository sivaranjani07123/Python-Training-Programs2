a = int(input("Enter base: "))
b = int(input("Enter power: "))
result = 1
for _ in range(b):
    result *= a
print(result)