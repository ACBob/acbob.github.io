#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#Oh christ, Four Million.


a = 1
b = 2
c = 0

for i in range(4000000):
    a,b = b,b+a
    if b % 2 == 0:
        c+=b
print(c)


#HOLEE SHIT DOES IT TAKE AGES.
#I actually made this in scratch not too long ago and it was faster.
