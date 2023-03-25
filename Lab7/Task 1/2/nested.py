students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])
    
scores = list([students[1] for student in students])
secondlowest = sorted(scores)[1]
    
names = [student[0] for student in students if student[1] == secondlowest]
    
for name in sorted(names):
    print(name)