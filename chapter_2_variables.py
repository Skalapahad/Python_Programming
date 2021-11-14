#it is an string
a = "satyam"
b = "subham"
c = "mina"
# it is an integer
d = 34
e = "56"
# it is a floating point number 
f = 67.34
g = 99.9

a = 0
password = "Xyz321"
while a <= 3:
    password = "Xyz321"
    user_password = int(input("Enter Your Password :"))
    if password == user_password:
        print("It is a Match .")
        break
    a+=1
else:
    print("Wrong Password , Try Again Later")
