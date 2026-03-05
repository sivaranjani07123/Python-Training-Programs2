a=input("Enter a :").strip()
b=input("Enter b :").strip()
if b=="0":
    print(1)
else:
    print(pow(int(a[-1]),int(b[-3:]),10))#pow(base,exponent,mod)(2^5=32%10)