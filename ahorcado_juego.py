import random


def obtener_palabra_secreta() -> str:
    palabras = [
        "python",
        "javascript",
        "java",
        "angular",
        "react",
        "node",
        "git",
        "bootstrap",
        "tailwind",
        "astro",
    ]
    return random.choice(palabras)

def progreso(palabra_secreta, letras_adivinadas):
    adivinado = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"
    return adivinado

def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 9
    game_over = False
    
    print("Bienvenido al juego del Ahorcado")
    print(f"tenes {intentos} intentos para adivinar la palabra")
    print(progreso(palabra_secreta, letras_adivinadas))

    while not game_over and intentos > 0:
        adivinanza = input("introduce una letra: ").lower()
        
        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("introduce solo una letra (solo letras)")
        elif adivinanza in letras_adivinadas:
            print("letra repetida")
        else:
            letras_adivinadas.append(adivinanza)
            if adivinanza in palabra_secreta:
                print(f"la letra {adivinanza} esta en la palabra")
            else:
                intentos -= 1
                print(f"Error te quedan {intentos} intentos")
                
        progreso_actual = progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)
        
        if "_" not in progreso_actual:
            game_over = True
            print(f"Ganaste la palabra era {palabra_secreta.capitalize()}")  
            play_again()      
    if intentos == 0:
        print(f"perdiste tonto la palabra era {palabra_secreta.capitalize()}")
        play_again()

def play_again():
    play = input("Quieres Jugar otra vez?(Y/N):")
    play = play.upper()
    if play == "Y":
        juego_ahorcado()
    elif play == "N":
        print("Hasta Luego")
    else:
        print("introduce una opcion valida")
        play_again()
juego_ahorcado()