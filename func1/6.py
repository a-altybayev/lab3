str = str(input())
def reverse(str):
    mylist = str.split()
    mylist.reverse()
    res = ''
    for i in mylist:
        res+= i + ' '
    return res
ans = reverse(str)
print(ans)