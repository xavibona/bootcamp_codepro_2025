p_objetivo = 'perro'
lista_objetivo = list(p_objetivo)
intentos = 6
tamano = 5
print(f'Bienvenido a Wordle\nInstrucciones de juego:\nTenes que adivinar una palabra de 5 letras en 6 intentos\nSi la letra esta en la posicion correcta sale asi: [A]\nSi la letra esta en la palabra pero no en la misma posicion sale asi: (A)\nSi la letra no existe sale sin nada\n--------------')
while intentos > 0: #Este bucle es cdda intento
    p_usuario = input('Ingrese una palabra de 5 letras')
    while len(p_usuario) != tamano: #Validador del tamaño de la palabra
        p_usuario = input('Tu palabra no tiene 5 letras, Ingrese otra')
    lista_usuario = list(p_usuario)
    lista_comparada = []
    lista_colores = []

    for ind_letra in range(tamano): #Este bucle es el que compara las letras 
        if lista_usuario[ind_letra] == lista_objetivo[ind_letra]: #Letra en lugar que corresponde
            lista_comparada.append(f'[{lista_usuario[ind_letra]}]')
            lista_colores.append('🟩')

        elif lista_usuario[ind_letra] in lista_objetivo: #Esta pero en otro lugar
            lista_comparada.append(f'({lista_usuario[ind_letra]})')
            lista_colores.append('🟨')

        else: #No existe
            lista_comparada.append(f'{lista_usuario[ind_letra]}')
            lista_colores.append('🟥')

    print(lista_comparada)
    print(lista_colores) #Se imprime la palabra y los colores

    if p_usuario == p_objetivo:
        print('Enhorabuena. Has ganado tio.')
        break

    intentos = intentos - 1 #Este va arriba asi cuando llega a cero se detiene
    if intentos == 0:
        print('Juego Terminado. Perdiste.') # :(s