#Password must contain 8 chars
#Has a digit
#Has an uppercase letter

Pass=input("Enter The Password: ")
class PasswordError(Exception):
    pass
Digits=False
Ucase=False
def Validator():
    global Digits, Ucase
    if len(Pass)<8:
        raise PasswordError("Password Must Contain atleast 8 characters")
    for i in Pass:
        if i >= "0" and i<="9":
            Digits=True
        if i>= "A" and i<="Z":
            Ucase=True
    if not Digits:
        raise PasswordError("Must contain atleast one digit")
    if not Ucase:
        raise PasswordError("Must contain atleast one capital letter")
try:
    Validator()
except PasswordError as a:
    print(a)
else:
    print("Success")
finally:
    print("Done")