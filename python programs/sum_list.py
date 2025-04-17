list = [1,2,3,4,5,16,12,18]

#output= 52


def even_sum(list):
    result = 0
    for i in list:
        if i % 2 == 0:
            result = i + result

    return result

output =even_sum(list)
print(f'even sum :', output)

def odd_sum(list):
    result = 0
    for i in list:
        if i % 2 != 0:
            result = i + result
    return result

output = odd_sum(list)
print(f'odd sum : ',output)