import random

while True:
    print('1. Lancia il dado\n2. Esci')
    user = int(input())
    if user == 1:
        num = random.randint(1,6)
        print('Numero generato : ',num)
    else:
        break