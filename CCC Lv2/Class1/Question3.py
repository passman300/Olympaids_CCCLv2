n = int(input())
stringslist = []

def Convert(string):
    list1=[]
    list1[:0]=string
    return list1


for i in range(n):
    strings = input()
    strings = ''.join([i for i in strings if not i.isdigit()])
    stringslist.append(strings)

print(stringslist)
for i in range(len(stringslist)):
    Strabc = stringslist[i]
    abc = Convert(Strabc)
    cba = stringslist[i][::-1]
    cba = Convert(cba)

    finalabc = []
    for j in range(0, len(abc)):
        if abc[j] == "(":
            if cba[j] == ")":
                finalabc.append(abc[j])
                finalabc.append(cba[j])
    print(abc)
    print(finalabc)
    if finalabc == abc:
        print("YES")
    else:
        print("NO")
