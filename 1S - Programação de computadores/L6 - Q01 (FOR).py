import random

n = int(input('Informe a quantidade de números: '))
numbers = []
for counter in range(n): numbers.append(random.randint(0, 9))
repetition = []
for counter in range(10): repetition.append(numbers.count(counter))
print(150 * '=')
print(f'Os números gerados foram: {numbers}.')
print(f'As repetições foram:\n0 => {repetition[0]}   1 => {repetition[1]}   2 => {repetition[2]}   3 => {repetition[3]}   4 => {repetition[4]}\n5 => {repetition[5]}   6 => {repetition[6]}   7 => {repetition[7]}   8 => {repetition[8]}   9 => {repetition[9]}')
print(150 * '=')