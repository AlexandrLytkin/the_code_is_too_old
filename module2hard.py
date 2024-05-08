from random import randint


def trap(n):
    cont = []
    unique = ''
    for i in range(1, n):
        for j in range(1, n):
            if i + j == n and i != j:
                if [j, i] in cont:
                    continue
                cont.append([i, j])
                unique += str(i) + str(j)

    return f'{n} - {unique}\nПоздравляю вас не раздавят, сокровище на верхней полке'


#  way 1
# n = randint(3, 20)
# print('Рандом решит твою судьбу')

#  way 2
n = int(input("Привет Indiana J. введи число и если оно будет кратно сумме каждой пары то вы будете жить ;): "))

indiana_jones = trap(n)
print(indiana_jones)
