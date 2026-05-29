def average(*x):
    y=sum(x)/len(x)
    print(y)
z=[int(input("enter marks")) for i in range(5)]
average(*z)