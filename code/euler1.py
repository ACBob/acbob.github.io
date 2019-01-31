#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#..Easy enough.

a = 3
b = 5
c = 0

for i in range(1000):
    if i % a == 0:
        c+=i
    elif i % b == 0:
        c+=i
print(c)

#See? took me five minutes.
