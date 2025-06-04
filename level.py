def choose_level(n_pregunta, p_level):
    
    # Construir lógica para escoger el nivel
    ##################################################
    if n_pregunta <= p_level:
        level = 'basicas'
    elif n_pregunta <= 2 * p_level:
        level = 'intermedias'
    elif n_pregunta <= 3 * p_level:
        level = 'avanzadas'
    else:
        # En caso de que se pase del límite (no debería pasar en este juego, pero es buena práctica)
        level = None 
    ##################################################
    
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias
    print(choose_level(1, 3)) # basicas
    print(choose_level(6, 2)) # avanzadas
    print(choose_level(0, 5)) # basicas (aunque no se use n_pregunta=0)
    print(choose_level(7, 1)) # avanzadas