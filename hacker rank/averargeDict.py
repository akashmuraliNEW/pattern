n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
list1 = student_marks[query_name]
avg=0
num=0
for i in list1:
    num+=1
    avg+=i
avg = avg/num   
print(f'{avg:.2f}')
    