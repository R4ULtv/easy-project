import time 
import random

out = False

while out == False:
    name = input('Come ti chiami ? ')
    print('Yo', name, 'Giochiamo !!!')

    words = ['lastra','farmacia','zero','marzo','minatore','rivista','messaggio','chiesa','cane','temperatura','conte','nonno','grappolo','martello']
    word = random.choice(words)

    guesses = ''
    turns = 5
    while turns > 0:
        failed = 0

        for char in word:
            if char in guesses:
                print(char,end='')
            else:
                print('_',end='')
                failed += 1

        if failed == 0:
            print('\nHai vinto!!!')
            n = input('Vuoi giocare ancora ? si/no\n')
            if n == 'si':
                break
            elif n == 'no':
                out = True
                break

        guess = input('\nIndovina la parola con un carattere : ')
        guesses += guess

        if guess not in word:
            turns -= 1
            print('Sbagliato')
            print('Hai ancora', turns,'turni per indovinare la parola')
            if turns == 0:
                print('Hai perso!!!')
                n = input('Vuoi giocare ancora ? si/no\n')
                if n == 'si':
                    break
                elif n == 'no':
                    out = True
                    break

