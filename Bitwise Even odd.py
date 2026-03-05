n = int(input("Enter the number: "))
if n & 1:
    print(True)
    print(f"{n} is odd")
else:
    print(False)
    print(f"{n} is even")