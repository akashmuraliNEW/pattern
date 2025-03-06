list=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    list+=[[name,score]]
# print(list,score)
secLowest=score
smalScore = secLowest
for scores in list:
    if scores[1]<smalScore:
        smalScore = scores[1]
# print(largScore)
for scores in list:
    if smalScore<scores[1]<secLowest:
        secLowest = scores[1]
# print(secLowest)
finaList = []
for result in list:
    if result[1]==secLowest:
        finaList+=[result[0]]
lenList = 0
for i in finaList:
    lenList+=1

if lenList>1:
    for i in range(lenList-1):
        if finaList[i]>finaList[i+1]:
            finaList[i],finaList[i+1]=finaList[i+1],finaList[i]  
    for names in finaList:
        print(names)
else:
    print(finaList[0])
