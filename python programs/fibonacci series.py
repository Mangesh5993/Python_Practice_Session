
inp=int(input('enter the number :'))

# [ 0,1,1,2,3,5,8,13,21,34,55,...]
#Fibonacci sequence, the sequence of numbers 1, 1, 2, 3, 5, 8, 13, 21, â€¦, each of which, after the second, is the sum of the two previous numbers
#output =[0,1,1,2,3,5,8,13,21,34]

def fibonacci_series(inp):
    a,b = 0,1
    result = []
    for _ in range(inp): # here _ is using when there are repeated values , also like I don't need values i just want loop
        a,b = b, a+b
        result.append(a)
    return result

output= fibonacci_series(inp)
print(output)

