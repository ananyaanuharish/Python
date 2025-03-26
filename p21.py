#bitwise
# &,|,^,-,<<,>>
# and & 1 1 = 1 otherwise 0
a = 5
# 0b0101 binary value for 5
b = 3
# 0b0011 binary value for 3
result = a & b
print(f"{a} & {b} = {result}")

# or | 1 1 = 1,  1 0=1, 0 1=1, 0 0=0
result = a | b
print(f"{a} | {b} = {result}")

# xor ^, 1 1=0, 1 0=1, 0 1=1, 0 0=0
result = a^b
print(f"{a} ^ {b} = {result}")

#bitwise not ~
# ~x = -(x+1)
result = ~a
print(f"~{a} = {result}")
result = ~b
print(f"~{b} = {result}")

# left  shift <<
# x<< n = x*(2^n)
x = 5
result = x << 1
print(f"{x} << 1 ={result}")

#right shift >>
# x >> n = x // (2^n)
x = 5
result = x >> 1