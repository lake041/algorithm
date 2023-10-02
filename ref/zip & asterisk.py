K = [95, 100, 80, 90, 80]
E = [90, 100, 90, 80, 85]
M = [90, 95, 90, 90, 95]
H = [90, 100, 95, 90, 100]

for idx, grade in enumerate(zip(K, E, M, H)):
    print(f"{idx+1}번 학생 성적 = {grade}")
print()

grades = [K, E, M, H]
for idx, grade in enumerate(zip(*grades)):
    print(f"{idx+1}번 학생 성적 = {grade}")