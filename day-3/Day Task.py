Contact={}
while True:
    print("\n1. Add User\n2. Search By Name\n3. Update\n4. Delete\n5. List Sort\n6. Exit")
    x=int(input("Enter A number from 1 to 6: "))
    match x:
        case 1:
            a=input("Type user name to add: ")
            b=int(input("Enter ph to add: "))
            Contact[a]=b
        case 2:
            c=input("Type Key For Search: ")
            print(Contact.get(c))
        case 3:
            d=input("Type user name to add: ")
            e=int(input("Enter ph to add: "))
            Contact[d]=e
        case 4:
            f=input("enter key to delete: ")
            del Contact[f]
        case 5:
            Contact=dict(sorted(Contact.items()))
        case 6:
            print("Exiting: ")
            break
        case _:
            print("enter a valid number: ")
