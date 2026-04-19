num = 1
while num <= 10:
    print(num)
    num += 1

password = input("What is the Password: ")
if len(password) <= 8:
    print("incorrect Password")
else:
    print("Correct Password")

for sqr in range(1,6):
    print(sqr*sqr)


for count in range(1,20):
    if count %2 == 0 :
          print(count)
  
for numbers in range(1,10):
  if numbers == 7:
    break
  print(numbers)


for counting in range(1, 10):
    if counting == 4:
        continue   
    print(counting)

for row in range(3):          
    for col in range(3):      
        print("*", end=" ")  
    print()                   