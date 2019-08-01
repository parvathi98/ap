numa = int(input("Enter any number:"))
flag = numa%2
if flag == 0:
    print(numa, "is an even number")
elif flag == 1:
    print(numa, "is an odd number")
else:
    print("Error, Invalid input")
