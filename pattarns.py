""" *
    * * """

num=5
for i in range (1,num+1):
    print("* "*i)
print("\n\n\n\n\n")





'''* * *
   * *
   *'''

num=5
for i in range (num,0,-1):
    print("* "*i)
print("\n\n\n\n\n")





""" * * *
      * *
        * """

num = 5
for i in range(num, 0, -1):
       sp = "  "*(num-i)   
       st = "* "*i
       print(sp+st)
print("\n\n\n\n\n")






'''  *
   * *
 * * *'''

num= 5
for i in range(1,num+1):
    sp="  "*(num-i)
    st="* "*i
    print(sp+st)
print("\n\n\n\n\n")








'''          *
           * * *
         * * * * *'''


num = 5
for i in range(1, num + 1):
    sp = "  " * (num - i)
    st = "* " * (2*i - 1)
    print(sp + st)
print("\n\n\n\n\n")






    

'''* * * * *
   *     * *
   *   *   *
   * *     *
   * * * * *'''


n = 5
for i in range(n):
    for j in range(n):
        if (i == 0 or j == 0 or i == n-1 or j == n-1 or i + j == n-1):
            print("* ", end="")
        else:
            print("  ", end="")
    print()
print("\n\n\n\n\n")








'''  *
     *
 * * + * *
     *
     *'''


n = 5
mid = n // 2
for i in range(n):
    for j in range(n):
        if i == mid and j == mid:
            print("+ ", end="")
        elif i == mid or j == mid:
            print("* ", end="")
        else:
            print("  ", end="")
    print()









       


