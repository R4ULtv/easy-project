from random import randint

list = ['Carta', 'Forbice', 'Sasso']

rand = list[randint(0,2)]
player = False
while player == False:
    player = input('Carta, Forbice, Sasso ?')
    if player == rand:
        print('Pareggio!!!')
    elif player == 'Sasso': 
        if rand == "Carta":
            print('Hai perso!!!')
        else:
            print("Hai vinto!!!", player, "spacca", rand)
    elif player == "Carta":
        if rand == "Forbice":
            print("Hai perso!!!", rand, "taglia", player)
        else:
            print("Hai vinto!!!", player, "copre", rand)
    elif player == "Forbice":
        if rand == "Sasso":
            print("Hai perso!!!", rand, "spacca", player)
        else:
            print("Hai vinto!!!", player, "taglia", rand)
    else:
        print("Input non valido. Controlla quelli che scrivi.")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    rand = list[randint(0,2)]