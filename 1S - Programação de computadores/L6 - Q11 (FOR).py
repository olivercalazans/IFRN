import random

letter = ['A', 'B', 'C', 'D','E']
right = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E']
students = ['Charles', 'Aron', 'Matheus', 'Marciano', 'Kalvin', 'Cazuí', 'Mellyssa', 'Alice', 'Carol', 'Luíza']
exams = []

for name in students:
    exam = []
    exam.append(name)
    for counter in range(10):
        number = random.randint(0,4)
        exam.append(letter[number])
    exams.append(exam)

for sublist in exams:
    corrects = 0
    for counter in range(10):
        if right[counter] == sublist[counter + 1]:
            corrects += 1
    sublist.append(corrects)

new_list = []
for counter in range(11):
    for student in exams:
        if counter == student[-1]:
            new_list.insert(0, student)

print(150 * '=')
print(f'Gabarito: {right}')
for student in new_list:
    print(f'O aluno(a) {student[0]} acertou {student[-1]}. Respostas: {student[1:11]}.')
print(150 * '=')
