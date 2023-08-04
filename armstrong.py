n=input("Enter a number :")
l=len(n)
n=int(n)
a=n
arm=0
for i in range(l+1):
    b=a%10
    a=a/10
    arm=arm+(b**l)
if (arm != n):
    print("It is not an Armstrong no.")
else:
    print("It is an Armstrong no.")
