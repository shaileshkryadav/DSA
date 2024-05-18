num1 = 11
num2 = num1

print("The number1 is ", num1 , "Its address is", id(num1))
print("the number2 is ", num2, "its address is ", id(num2))

num2 = 23
print("The new address of num2 is ", id(num2))

dir1 = {
    "value":11
}
dir2 = dir1
print("The adress of dir1 is ", id(dir1))
print("The adress of dir2 is ", id(dir2))

dir2["value"] = 33
print("The new value of dir1 is ", dir1["value"]," and the address is", id(dir1))