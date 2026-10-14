# q1 -> What is the output of the following, and why?

s="python"
print(s[0],s[-1],s[6])

# output
# IndexError: string index out of range

# ================

# q2 ->What is the difference between positive and negative indexing? Given s = "Hello", what does s[-2] return?

s="hello"
print(s[-2])

# output
# l

# ===================

# q3->What happens when you access an index that is out of range in a string? How is this different from slicing out of range?

product="zebronics"
print(product[10])
print(product[1:10])

# output
# ebronics

# ============================

# q4 -> how do find the index of first and last

actor="naveenkumar"
fa=actor.find("e")
la=actor.rfind("e")
print(fa,la)

# output
# 3,4

# ==========================

# q5->what is the output of the followinf and explain how negative indexing resolve?

company="techpanda"
print(company[-1],company[-3],company[-6])

# output
# a n h

# ============================

# q6->what is the syntex for sring in slicing in pyhton?
# string[start:end:step]

doctor="vetrimaran"
print(doctor[1:5])

# output
# etri

# =================================

# q7->what is output of the folowing slicing, and why?

movie="tamizhagavetrikondan"
print(movie[0:5])
print(movie[5:])
print(movie[:5])
print(movie[:])

# output

# tamiz
# hagavetrikondan
# tamiz
# tamizhagavetrikondan

# ================================

# q8->what happen when start is greater then stop in a slice with a positive step? what is the output?

program="python"
print(program[4:1])

# output
# ""

# =========================

# q9-> how can you extract the last 3 caracter of a sting using slicing without knowing ins length?

name="naveenkumar"
print(name[-3:])

# output
# mar

# ============================

# q10->what is the difference between these two slices?what does each return?

company="techpanda"
print(company[::1])
print(company[::2])
print(company[::3])
print(company[1::2])

# output

# techpanda
# tcpna
# thn
# ehad

# ==========================

# q11->reverse a sring using slicing

coding="python"
print(coding[::-1])

# output
# nohtyp

# =============================

# q12->explain negative-step slicing

vehicle="rollsroys"

print(vehicle[::-1])
print(vehicle[::-2])
print(vehicle[6:1:-1])

# output
# syorsllor
# soslr
# orsll
# ==========================

# q13-> extracr every 3rd character starting from index 1?

words="a1b2c3d4e5"
print(words[1::2])

# output
# 12345

# q14->negative step slicing

code="python"
print(code[5:0:-1])
print(code[5::-1])
print(code[:0:-1])

# output
# nohty
# nohtyp
# nohty
# =========================

# q15->negative step slicing with out of range indices 

s="hello"
print(s[100::-1])
print(s[::-100])

# output
# olleh
# o

# q16->extract the middle portion dynamically

s="abcdefghij"
print(s[2:-1])

# output
# cdefghi

# ===============================

# q17->check whether a string is a palindrome using slicing

s="racecar" 
print(s == s[::-1])

# output
#true

# ====================================

# q18->why does slicing not raise an error sor out of range indices?

animal="butterfly"

print(animal[1:100])
print(animal[-100:3])
print(animal[1000:200])

# output
# utterfly
# but

# q19->how can you replace "world" with "python" using slicing and concoatenation, since strings are immutable?

name="hello world"
s=name[:6]+"python"
print(s)

# output
# hello python

# ==============================

# q20->using the slice() object?

s="0123456789"
sliceing=slice(1,8,2)
print(s[sliceing])

# output
# 1357