answer_system = int(input())
answer_student = int(input())

if str(answer_system) == str(answer_system)[::-1] and answer_student == 1:
    print("YES")
else:
    print("NO")
