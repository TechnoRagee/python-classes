# So I am creating a login System Logic for website 


user = []
Email = input("Enter your Email ID :")
Password = input("Enter Your Password")
name = Email.split("@")[0]
user.append(name)
if name in user and "@" in Email and "gmail" in Email:
    print("Correct Email ID")
else:
    print("Not an Valid Id")
if len(Password) <= 8:
    print("incorrect Password")
else:
    print("Correct Password")