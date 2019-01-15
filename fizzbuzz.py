fizz = "fizz"
buzz = "buzz"
a = 3
b = 5
for i in range(101):
    if i % a == 0 and not i % b == 0:
        print(fizz)
    if i % b == 0 and not i % a == 0:
        print(buzz)
    if i  % a == 0 and i % b == 0:
        print(fizz + buzz)
    else:
        print(i)
