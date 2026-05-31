#firstly we created an empty dictionary
students={}

#using while True loop so that the loop runs until the user doesn't gives us the command to exit 
while True:
    print("\n----Result_Manager_Students")
    print("1. Add Student")
    print("2. View Students")
    print("3. Check Result")
    print("4. Exit")

    #let's take the input of choice from the user

    choice = input("Enter Your Choice:")

    #Add Student
    if choice=="1":
        name=input("Enter Student Name:")
        marks=int(input("Enter Marks:"))
        students[name]=marks
        print(f"{name} Successfully Added")

    #view students
    elif choice=="2":
        if not students:
            print("Students Not Found")
        else:
            for name,marks in students.items():
                print(name,":",marks)

    #Check Result
    elif choice=="3":
        name=input("Enter Student Name:")

        if name in students:
            marks=students[name]

            if marks >=40:
                print("PASS")
            else:
                print("FAIL")

        else:
            print("Student Not Found !")

    #Exit
    elif choice=="4":
        print("Exiting....")
        break

    #If an invalid choice is entered by the user
    else:
        print("Invalid Input")