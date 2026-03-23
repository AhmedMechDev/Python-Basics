print("     Welcome to the compny programm 😀 \n ")
while True:
    check=input("Did you want to exit out the program: ").lower()
    if check=="yes":
        break
    else:
        txt=open('company.txt',"a")
        name=input("Enter the employee name: ")
        txt.write("\nName: ")
        txt.write(name)
        code=input("Enter the employee code: ")
        txt.write("\nCode: ")
        txt.write(code)
        txt.write("\n--------------------------------------")