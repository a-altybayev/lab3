def unique(list):
    unique_list = []
    for i in list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list
a = input()
b= [int(x) for x in a.split()]
print(unique(b))