# file write method

# file=open("naveen.txt","w")
# file.write("hello naveen welcome\nhi welcome harrish\nhi welcome sneha ")
# file.close()

# ===================================

# file read method

# file=open("naveen.txt","r")
# print(file.read())
# file.close()

# readline

# file=open("naveen.txt","r")
# print(file.readline())
# file.close()

# readlines

# file=open("naveen.txt","r")
# print(file.readlines())
# file.close()

# ===========================

# appaend mode

# file=open("naveen.txt","a")
# file.write("\nhi gokul welcome")
# file.close()

# with open("naveen.txt","w") as data:
#     data.write("end the file handling")

# with open("naveen.txt","r") as data:
#     print(data.read())

with open("naveen.txt","r+") as m:
  
    m.write("hihihihiihihihihihihihihihihih")
    print(m.read())