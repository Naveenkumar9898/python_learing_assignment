# exception handling

# zero divisionError
# try:
#     a=10
#     b=2
#     print(a/b)
# except:
#     print("something wrong")

# output
# 5.0

# =================================

# try:
#     num=int(input("enter the number"))
#     print(100/num)
# except ValueError:
#     print("enter number only")
# except ZeroDivisionError:
#     print("connot divide by zero")

# ===========================================

# using else and finally

try:
    num=int(input("enter the number"))
    multi=int(input("enter the divide value"))
    print(num/multi)

except ZeroDivisionError:
    print("cannot divide vy zero ")

else:
    print("no error occured")

finally:
    print("program executed")


    