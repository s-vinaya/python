def binsearch(A, a, b, q):
    m=int((a+b)/2)
    if (q> A[m]):
        binsearch(A, m, b, q)
    elif (q<A[m]):
        binsearch(A, a, m, q)
    elif (q== A[m]):
        print("the element is found on index:" )
        print(m+1)
    else:
        print("item not present in the list")
n=int(input("enter the total no. of elements: "r))
print("enter the elements:")
A=[]
for i in range(n):
    a=int(input())
    A.append(a)
print("enter the no. to be searched:")
q=int(input())
binsearch(A, 0, n-1, q)
