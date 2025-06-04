def validate(opciones, eleccion):
    # Definir validación de eleccion
    ##########################################################################
    while eleccion not in opciones:
        print("Opción no válida, intente de nuevo.")
        eleccion = input('Ingresa una Opción: ').lower()
    ##########################################################################
    return eleccion


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    eleccion_validada = validate(numeros, eleccion)
    print(f"Opción validada: {eleccion_validada}")

    letras = ['a', 'b', 'c', 'd']
    eleccion_letras = input('Ingresa una Opción de letra: ').lower()
    eleccion_letras_validada = validate(letras, eleccion_letras)
    print(f"Opción de letra validada: {eleccion_letras_validada}")