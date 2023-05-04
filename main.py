s='a,2,b,5,c,8,a,4,e,11'
s=s.split(',')
answer={}
for i in range(0,len(s),2):
    if s[i] not in answer:
        answer[s[i]]=int(s[i+1])
    else:
        answer[s[i]]+=int(s[i+1])
print(answer)




