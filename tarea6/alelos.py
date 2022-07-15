# Tarea
##Crear un módulo alelos.py con las tres funciones de "Creación de la población", "Cuantificación de frecuencias de alelos" y "Creación de la población hijo". Cada función debe tener una sección de explicación de lo que hace, la explicación de las variables de entrrada y salida.
##Crear un Júpiter Notebook tarea6_alelos.ipynb, cargar el módulo alelos y ejecutar las funciones hasta obtener la generación 100. Asegurarse que este cuaderno de jupyter tenga sus datos personales, texto de explicación del ejercicio y de los resultados. Inserte al menos una imagen (logo de Ikiam). Asegurarse que el cuaderno tiene los resultados de ejecución de los bloques de código.
##Crear un repositorio en GitHub de nombre tarea6 y guardar los dos archivos de la tarea. El repositorio debe tener una Readme con los detalles de la actividad.
##Pegar el enlace del repositorio en la actividad T6_alelos de Moodle

# FUNCIÓN 1. de creación de una población con alelos al azar

import scipy 

def build_population(N, p):
    population = []
    for i in range(N):
        allele1 = "A"
        if scipy.random.rand() > p:
            allele1 = "a"
        allele2 = "A"
        if scipy.random.rand() > p:
            allele2 = "a"
        population.append((allele1, allele2))
    return population


def compute_frequencies(population):
   
    AA = population.count(("A", "A"))
    Aa = population.count(("A", "a"))
    aA = population.count(("a", "A"))
    aa = population.count(("a", "a"))
    return({"AA": AA, "aa": aa, "Aa": Aa, "aA": aA})


def reproduce_population(population):
    new_generation = []
    N = len(population)
    for i in range(N):
        # random integer between 0 and N-1
        dad = scipy.random.randint(N)
        mom = scipy.random.randint(N)
        # which chromosome comes from mom
        chr_mom = scipy.random.randint(2)
        offspring = (population[mom][chr_mom], population[dad][1 - chr_mom])
        #if offspring == ("a", "a"): 
          #next()
        new_generation.append(offspring)
    return new_generation

