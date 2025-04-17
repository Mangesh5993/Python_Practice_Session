
list = [1,2,3,4,5,16,12,18]

#output = [ 2,4,12,16,18]
result = []
def even_list(list):
    for i in list:
        if i % 2 == 0:
            result.append(i)
    return result

output=even_list(list)
print(output)