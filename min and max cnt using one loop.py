n=int(input())
min=n%10
max=n%10
minc=maxc=0
while n:
    r=n%10
    n=n//10
    if r==min:
        minc+=1
    elif r<min:
        min=r
        minc=1
    if r==max:
        maxc+=1
    elif r>max:
        max=r
        maxc=1
print(min,minc)
print(max,maxc)
