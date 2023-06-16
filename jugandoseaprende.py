import random

print('Bienvenido al famoso juego piedra, papel o tijera'.capitalize())
print ('Hoy jugarás contra una opción aleatoria del programa 🤖'.capitalize())
print ('Que ''\n''gane ''\n''el ''\n''mejor !!! 🤩🤓🤝🏼'.capitalize())

user_name = input('Para iniciar: ''\n''Cómo te llamas? Escribe tu nombre aqui ----> ')
user_input = input('Escoge una de estas opciones para jugar: piedra, papel o tijera ---> ').lower().strip()

#Se establecen las opciones para ejecutar el metodo random.randit que selecciona una opcion dentro de el numero de opciones posibles.
options = ['piedra','papel','tijera']

#Validar el input del usuario. Si es diferente a alguna de las opciones = ingrese una opción válida
while user_input != 'piedra' and user_input != 'papel' and user_input != 'tijera':
    print(f'{user_name}, Por favor ingresa una opción válida')
    user_input = input('Escoge una de estas opciones para jugar: piedra, papel o tijera ---> ').lower().strip()

'''
#Otra forma para hacer la validación con while y break
while(True):
    if user_input in options:
        break
    else:
        print ('Elige una opción válida para jugar')
        user_input = input('Escoge una de estas opciones para jugar: piedra, papel o tijera ---> ').lower().strip()
'''

computer_input= options[random.randint(0,2)]
print('El programa escogió: ', computer_input)

if computer_input == 'piedra':
    if user_input == 'piedra':
        print('Es un empate')
    elif user_input == 'papel':
        print('El papel envuelve a la piedra y le gana')
        print(f'Ganó {user_name} !!! 🤩🎉👏🏼👏🏼'.upper())
    elif user_input == 'tijera':
        print('La piedra le gana a la tijera porque la tijera no corta la piedra, pero la piedra si puede destruir a la tijera')
        print(f'{user_name}, has perdido 🥲🫣🫤. Gana el programa🤖🤖🤖')

elif computer_input == 'papel':
    if user_input == 'piedra':
        print('El papel envuelve a la piedra')
        print(f'{user_name}, has perdido 🥲🫣🫤. Gana el programa🤖🤖🤖')
    elif user_input == 'papel':
        print('Es un empate')
    elif user_input == 'tijera':
        print('La tijera corta el papel dejando un claro ganador')
        print(f'El ganador es: {user_name}!!! 🤩🎉👏🏼👏🏼'.upper()) 

elif computer_input == 'tijera':
    if user_input == 'piedra':
        print('La piedra rompe la tijera de un karatazo')
        print(f'El feliz ganador es: {user_name}!!! 🤩🎉👏🏼👏🏼'.upper())
    elif user_input == 'papel':
        print('La embarrada bro porque la tijera corta el papel')
        print(f'Esta ronda la perdiste: {user_name} 🥲🫣🫤. Gana el programa🤖🤖🤖')
    elif user_input == 'tijera':
        print('Bro, al menos no perdiste. Es un empate')