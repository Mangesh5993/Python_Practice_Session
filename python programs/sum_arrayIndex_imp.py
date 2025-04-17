
# Find the index of arrays having total = 9  from the list
list = [2,7,11,15]

Target = 9

output = [0,1]


def sum_array(n):
    empt_dict = {}
    result = []
    for i in range(len(list)): # itrating index of list
        diff = Target - list[i]
        if diff in empt_dict:
            result = [empt_dict[diff],i]
            return result
            break
        empt_dict[list[i]] = i



res=sum_array(list)
print(res)




