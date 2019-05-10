s = input()
K = int(input())

dict = [s]
for i in range(int(len(s))):
    for j in range(i+1,int(len(s))+1):
        tmp = s[i:j]
        if tmp != s and tmp not in dict:
            dict.append(s[i:j])
sorted_dict=sorted(dict)
print(sorted_dict[K-1])
