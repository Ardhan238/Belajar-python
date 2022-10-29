# Logika boolean / gerbang logika
# AND, OR, NOT, XOR

# AND
print ("============AND============\n")

a = False
b = False
c = a and b
print ("Data C = ", c)

a = False
b = True
c = a and b
print ("Data C = ", c)

a = True
b = False
c = a and b
print ("Data C = ", c)

a = True
b = True
c = a and b
print ("Data C = ", c)

print ("------------------------------------------\n")

# OR
print ("============OR============\n")

m = False
n = False
o = m or n
print ("Data O = ", o)

m = False
n = True
o = m or n
print ("Data O = ", o)

m = True
n = False
o = m or n
print ("Data O = ", o)

m = True
n = True
o = m or n
print ("Data O = ", o)

print ("------------------------------------------\n")

# NOT
print ("============NOT============\n")

p = False
q = not p
print ("Data Q = ", q)

p = True
q = not p
print ("Data Q = ", q)

print ("------------------------------------------\n")

# XOR
print ("============XOR============\n")

x = False
y = False
z = x ^ y
print ("Data Z = ", z)

x = False
y = True
z = x ^ y
print ("Data Z = ", z)

x = True
y = False
z = x ^ y
print ("Data Z = ", z)

x = True
y = True
z = x ^ y
print ("Data Z = ", z)