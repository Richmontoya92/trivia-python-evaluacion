import preguntas as p

def verificar(alternativas, eleccion):
    #devuelve el índice de elección dada
    letras = ['a', 'b', 'c','d']
    eleccion_idx = letras.index(eleccion)

    # generar lógica para determinar respuestas correctas
    ##########################################################################################
    # La alternativa correcta tiene un 1 en la segunda posición (indice 1)
    if alternativas[eleccion_idx][1] == 1:
        correcto = True
    else: 
        correcto = False
    ##########################################################################################
    return correcto


if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Prueba de respuesta correcta (asumiendo que 'alt_2' es la correcta y corresponde a 'b')
    respuesta_correcta = 'b' 
    print(f"Respuesta escogida: {respuesta_correcta}")
    print(f"¿Es correcta? {verificar(pregunta['alternativas'], respuesta_correcta)}") # Debería ser True

    print("\n---")
    
    # Prueba de respuesta incorrecta
    respuesta_incorrecta = 'a'
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    print(f"Respuesta escogida: {respuesta_incorrecta}")
    print(f"¿Es correcta? {verificar(pregunta['alternativas'], respuesta_incorrecta)}") # Debería ser False

    # Nota: para que estas pruebas sean más robustas, deberías mezclar las alternativas
    # antes de verificar, como se hará en main.py



