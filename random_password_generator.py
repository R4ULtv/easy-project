import random

passlen = int(input('Inserisci la lunghezza della password : '))

string = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'

p = "".join(random.sample(string,passlen ))
print (p)