lst = [1, 1, 2, 2, 3, 5, 5, 5]

output = {1: [0, 1], 2: [2, 3]}

from collections import Counter

list_count = Counter(lst)
print(list_count)


result = {}
for num in list_count:
    if list_count[num] >1:  #  num having count >1 : 1,2,5
        map_num = []
        for i in range(len(lst)): # index = 0,1,2,3,4,5,6,7
            if lst[i] == num:
                map_num.append(i)
        result[num] = map_num

print(result)


