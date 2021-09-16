import random

x = 1
y = 10

num = random.randint(x,y)

print('Indovina il numero tra ', x, ' e ', y)

for i in range(0,3):
    user = int(input('Prova un numero: '))
    if user == num:
        print('Hai indovinato bro !!!')
    else:
        print('Me spiace bro ritenta')
