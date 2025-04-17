
# Find the list of arrays having total = 9  from the list
list = [2,5,4,7,11,15]

target = 9

output = [[2,7],[5,4]]

result=[]

def find_required_array(n):
    target =9
    result = []
    for i in range(len(list)): # here i and j are the indexes [0,1,2,3,4,5]
        for j in range(i+1, len(list)): #
            if list[i] + list[j] == target:
                result.append([list[i],list[j]])

    return result

out = find_required_array(list)
print(out)


