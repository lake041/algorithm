value = 60

b = format(value, '#b') # 0b111100
o = format(value, '#o') # 0o74
h = format(value, '#x') # 0x3c

print(b)
print(o)
print(h)

b = format(value, 'b') # 111100
o = format(value, 'o') # 74
h = format(value, 'x') # 3c

print(b)
print(o)
print(h)

print(int('101',2))
print(int('202',3))
print(int('303',4))
print(int('404',5))
print(int('505',6))
print(int('ACF',16))