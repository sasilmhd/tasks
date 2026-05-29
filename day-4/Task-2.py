def safe_divide(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print(f"{x} can't be divided by zero")
x=int(input("Enter a Number: "))
y=0
safe_divide(x, y)