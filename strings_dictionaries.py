text = " '  hi my name is vareen   ' "
print(text.strip())
print(text.title())


email = input("What is your EmailID :")
if email.startswith("user") and "@" and "gmail"in email:
    print("you have entered the valid Email Id")
else:
    print("This is Not valid Email Id ")

student = {'name': 'Alice', 'age': 22}

for key in student:
    print(key)

student = {'name': 'Alice', 'age': 22}
for value in student.values():
    print(value)

town = {
    'A' : {
        'Name': 'vareen',
        'City': "Noida"
    },
    
    'B' : {
        'Name' : 'Sarthak',
        'City' : 'Bisarkh'
    }
}

print(town)
print(town.get('A', {}).get('City', 'Not Found'))

config = {'theme': 'dark'}

print(config.get('font_size', 12))