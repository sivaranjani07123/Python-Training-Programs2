a=input("Enter a:")
b=input("Enter b:")
if b=="0":
    print(1)
else:
    print(pow(int(a[-1]),int(b[-3:]),10))