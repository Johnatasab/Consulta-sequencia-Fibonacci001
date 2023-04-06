print('_'*30)
print('Sequência de Fibonacci')
print('_'*30)
n = int(input('Qual numero você quer consultar?:'))

t1 = int(0)
t2 = int(1)
t3 = int(0)
print('-'*30)

cont = 3
while n > t3:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1

if n == 0 or n == 1:
    print('O número digitado faz parte a seguência de Fibonacci')
elif n == t3:
    print('O número digitado faz parte da sequência de Fibonacci')
else:
    print('O número digitado, não faz parte da sequência de Fibonacci\n')
