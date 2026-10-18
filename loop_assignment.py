# find largest number

numbers=[7,8,5,2,4,6,2,0,45,522,42]

large=numbers[0]

for num in numbers:
    if num>large:
        large=num

print(large)

# output-522

# ============================================

# find and count vowls?

text="butterfly"
count=0

for i in text:
    if i in "aeiou":
     count +=1 

print(count)

# output-2

# ==================================

# find factorial number?

number=4
factorial=1
for i in range(1,number+1):
  factorial=factorial*i
print(factorial)

# output-24

# ============================================

# count positive numbers

numbers=[1,-5,-6,-4,2,4,-8,-10,4,7,3]
count=0
for i in numbers:
    if i>0:
        count+=1
print(count)

# output-6

# ================================================

#  count negative numbers
numbers=[1,-5,-6,-4,2,4,-8,-10,4,7,3]
count=0
for i in numbers:
     if i<0:
         count+=1
print(count)

# output-5