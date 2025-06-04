import preguntas as p
import random

def shuffle_alt(pregunta):
    #mezclar alternativas
    #######################################################################
    alternativas = pregunta['alternativas']
    random.shuffle(alternativas)
    #######################################################################
    
    return alternativas

if __name__ == '__main__':
    # si se ejecuta el  programa varias veces las alternativas debieran aparecer en distinto orden
    # a modo de ejemplo
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print("Original:", pregunta['alternativas'])
    print("Mezcladas:", shuffle_alt(pregunta))

    pregunta = p.pool_preguntas['intermedias']['pregunta_2']
    print("Original:", pregunta['alternativas'])
    print("Mezcladas:", shuffle_alt(pregunta))