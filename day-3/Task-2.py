dict1={
    "Abhi":50,
    "Abu":30,
    "Babu":55
}
for student, mark in dict1.items():
    if mark>=50:
        print(student,":",mark)