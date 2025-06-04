import preguntas as p

def print_pregunta(enunciado, alternativas):
    
    # Imprimir enunciado y alternativas
    ###############################################################
    print(enunciado[0]) # El enunciado es una lista, toma el primer elemento
    letras = ['A', 'B', 'C', 'D']
    for i, alt in enumerate(alternativas):
        print(f"{letras[i]}. {alt[0]}") # alt[0] es el texto de la alternativa
    ###############################################################
        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta_basica = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta_basica['enunciado'],pregunta_basica['alternativas'])
    
    print("\n---")

    pregunta_intermedia = p.pool_preguntas['intermedias']['pregunta_2']
    # Para probar con alternativas mezcladas, usamos shuffle_alt antes de imprimir
    from shuffle import shuffle_alt
    alternativas_mezcladas = shuffle_alt(pregunta_intermedia)
    print_pregunta(pregunta_intermedia['enunciado'], alternativas_mezcladas)
    
    # Ejemplo de cómo debería verse la salida
    # Enunciado básico 1
    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4