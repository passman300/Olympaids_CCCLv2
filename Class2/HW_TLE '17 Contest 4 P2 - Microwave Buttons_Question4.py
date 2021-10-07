def toSeconds(hh, mm, ss):
    output = hh * 3600 + mm * 60 + ss
    return output

#
# def toHHMMSS(seconds):
#
hh, mm, ss = input().split(":")
h1 = int(hh[0])
h2 = int(hh[1])
m1 = int(mm[0])
m2 = int(mm[1])
s1 = int(ss[0])
s2 = int(ss[1])
numbers = []
numbers[:0] = input()
numbers = [int(i) for i in numbers]
output_time = []
output_time.append(h1) #can't change the first hour

if h2 not in numbers:
    new_h2 = -1
    if (h2 - 1) in numbers:
        new_h2 = h2 - 1
        output_time.append(new_h2)

        sec_time = toSeconds(1, int(mm), int(ss))
        



    elif new_h2 == -1:
        output_time.append()