    user = int(input("write a number"))
    if user >= 0:
        print("yes it is position")

    else:
        print("negative number")


    Check_number = int(input("write a Number :"))

    if Check_number %2 == 0:
        print("Yes it is Even")
    else:
        print("No it is an Odd Number")

    Person = int(input("write your Age"))
    if Person >=18:
        print("Yes youre Eligible for Vote")
    else:
        print("No Youre Not Eligible for voting")

    Number = int(input("write a Number : "))
    if Number >=10:
        print("yes it is greater than 10")
        if Number %2 ==0:
            print("Yes it is Even")

    else:
        print("No it is not greater then 10 ")

    P1 = bool(input("Write an input:"))
    P2 = bool(input("Write an input:"))
    print (P1 and P1)
    print(P1 or P2)


    Student_marks = int(input("Write Overall Marks: "))
    if Student_marks >= 90:
        print("A")
    elif Student_marks>= 75:
        print("B")
    elif Student_marks >= 50:
        print("C")
    else:
        print("Fail")