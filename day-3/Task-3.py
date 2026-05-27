#By Using Reversed Function
str1="Blah Blah Blah"
x=reversed(str1)
y=",".join(x)
print(y)

#By Using Slicing
print(str1[::-1])

#By Using Loop
str2=""
for i in str1:
    str2=i+str2
print(str2)