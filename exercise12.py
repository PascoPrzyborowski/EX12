

#Task1

import time

secret =input("Input Secret phrase:")
time.sleep(1)
print(secret)
time.sleep(1)
Name =input("Input Name:")
time.sleep(1)
print(Name)
time.sleep(1)
Year =input("Input Year:")
time.sleep(1)
print(Year)
time.sleep(1)
print()
result = f"{secret}{Name}{str(Year)}"
x = result
print(result)
result1 = (list(reversed(x)))
print(result1)
xs = result1
s = ''.join(str(x) for x in xs)

#result3 = (reversed(result2))
print(s)