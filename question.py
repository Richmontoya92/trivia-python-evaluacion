import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
# Usaremos una copia para modificarla sin afectar el original
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################

def choose_q(dificultad):
    #escoger preguntas por dificultad
    preguntas_disponibles = p.pool_preguntas[dificultad]
    
    # usar opciones desde ambiente global
    global opciones
    
    # escoger una pregunta
    # Asegúrate de que n_elegido sea un número que corresponda a 'pregunta_X'
    if not opciones[dificultad]: # Si no quedan preguntas de esa dificultad
        return None, None # O manejar el error de otra forma

    n_elegido_idx = random.choice(opciones[dificultad])
    n_elegido = f'pregunta_{n_elegido_idx}'

    # eliminarla del ambiente global para no escogerla de nuevo
    opciones[dificultad].remove(n_elegido_idx)
    
    # escoger enunciado y alternativas mezcladas
    pregunta = preguntas_disponibles[n_elegido]
    alternativas = shuffle_alt(pregunta) # Llamar a shuffle_alt con la pregunta completa
    
    return pregunta['enunciado'], alternativas

if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    print("--- Básicas ---")
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    print("\n--- Intermedias ---")
    pregunta, alternativas = choose_q('intermedias')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')

    pregunta, alternativas = choose_q('intermedias')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')

    pregunta, alternativas = choose_q('intermedias')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')

    print("\n--- Avanzadas ---")
    pregunta, alternativas = choose_q('avanzadas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')

    pregunta, alternativas = choose_q('avanzadas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')

    pregunta, alternativas = choose_q('avanzadas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')