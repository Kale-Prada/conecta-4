from test import *

def find_n(elements, needle, n):
    """
    Devuelve True si en elements hay n o más ocurrencias de needle
    False si hay menos o si n < 0
    :param elements: list
    :param needle: int
    :param n: int
    :return: bool
    """
    #Siempre que n sea menor a 0 me devolverá False
    if n >= 0:
    #Inicializo índice "index" y contador "count"
        index = 0
        count = 0
    #Entra en la lista con el while, recorre la lista completa.
        while count < n and index < len(elements):
    #si lo encontramos, actualizamos el contador
            if needle == elements[index]:
                count += 1
    #avanzo al siguiente elemento
            index += 1
    #Devuelve el comparar count con n
        return count >= n
    else:
    #Siempre que n sea menor a 0 me devolverá False
        return False

def fine_one1(elements, needle):
    """
    Devuelve True si encuentra una o más ocurrencias de needle en la lista
    Le he llamado find_one1 porque esta es la primera versión en find_one se refactoriza
    el código.
    :param elements:list
    :param needle:int
    :return:bool
    """
    #Inicializamos bool que representa la condición de haber encontrado o no
    #Inicializo el índice "index"
    found = False
    index = 0

    # Mientras no encontramos o hayamos terminado con la lista
    while not found and index < len(elements):
    #observo si está en la posición actual y actualizo la condición
        if needle == elements[index]:
            found = True
    #continúo al siguiente elemento
        index = index + 1
    #devuelvo si hemos encontrado o no
    return found

def find_one(elements, needle):
    """
    Refactorizo el código (si quiero ver el original ver find_one1)
    Aplico principio de la ciberkinesis DRY - Don´t repeat yourself

    :param elements:list
    :param needle:int
    :return: find_n(elements, needle, 1) - bool
    """
    #Hago la llamada a find_n para que me encuentre el primer needle
    return find_n(elements, needle, 1)

def find_strike(elements, needle, n):
    """
    Devuelve True si en elements hay n o más needles seguidos. Están en racha.
    False si no se cumple lo anterior.

    :param elements:list
    :param needle:int
    :param n:int
    :return:bool
    """
    #Si n es mayor o igual a cero
    if n >= 0:
    #Inicializo el índice "index" a cero y el contador "count" a cero.
        index = 0
        count = 0
    #Se comenta en clase: la bandera del strike se comenta porque sin ella los assert también pasan.
    #Importante sumar index si el contador se vuelve a inicializar.
    #Se reinicializa el contador en cuanto uno no es el elemento.
        #strike = False
        while count < n and index < len(elements):
    #Si la aguja es igual al elemento
            if needle == elements[index]:
                #strike = True
    #Avanzamos con el contador
                count += 1
            else:
                #strike = False
    #Contador se vuelve a inicializar a cero. Porque no hay racha.
                count = 0
    #Sumamos al índice
            index += 1
        return count >= n #and strike
    else:
        return False

if __name__ == '__main__':
    #Llamada a la función con mis datos de prueba
    #¿Qué pasa si n = cero?
    elements = [1, 5, 7, 4]
    needle = 4
    n = 0
    resultado = find_strike([elements],needle, n)
    #Imprime el resultado en la consola para verificarlo
    print("Resultado de la prueba cuando n = 0:", resultado)

def make_list(length, filler):
    """
    Hacer una lista
    :param length:
    :param filler:
    :return: list
    """

    result = []
    index = 0
    while index < length:
        result.append(filler)
        index += 1
    return result

def index_first_element(elements, needle):
    """
    Obtiene el indice de un elemento determinado en una lista
    :param elements: mi lista
    :param needle: el elemento a buscar
    :return:
    """
    index = 0
    while index < len(elements):
        if needle == elements[index]:
            return index
        else:
            index += 1
    return None

def map_list(elements, transform):
    """
    Creo una lista nueva aplicando transform a cada elemento
    :param elements:
    :param transform:
    :return:
    """

    result = []
    for element in elements:
        result.append(transform(element))
    return result

def make_list_from_factory(length, factory):
    """
    Crea una lista de listas que son fabricadas por mi fábrica que es LinearBoard
    :param length:
    :param factory:
    :return:
    """
    result = []
    index = 0
    while index < length:
        result.append(factory())
        index += 1
    return result

def transpose(matrix):
    """
    Intercambia filas y columnas. Funciona con matrices no cuadradas.
    """
    if not matrix:
        return []
    height = len(matrix[0])
    result = []
    for i in range(height):
        sub_result = []
        for j in range(len(matrix)):
            sub_result.append(matrix[j][i])
        result.append(sub_result)
    return result

def displace(l, distancia, filler = None):
    n = len(l)
    result = []
    for i in range(n):
        index = i - distancia
        if 0 <= index < n:
            result.append(l[index])
        else:
            result.append(filler)
    return result

def displace_matrix(matrix, filler = None):
    d = []
    for i in range(len(matrix)):
        d.append(displace(matrix[i], i - 1, filler))
    return d

def reverse_list(elements):
    return elements[::-1]

def reverse_matrix(matrix):
    result = []
    for col in matrix:
        result.append(reverse_list(col))
    return result

def all_the_same_score(elements):
    """
    No controla lista vacía. De momento no pasa nada.
    """
    if not elements:
        return True
    first_element = elements[0]
    result = True
    for element in elements:
        if element != first_element:
            result = False
    return result

def colpase_matrix(matrix, empty = '.', sep = '|'):
    result = ''
    for elt in matrix:
        result = result + sep + colapse_list(elt, empty)
    return result[1:]

def colapse_list(elements, empty = '.'):
    result = ''
    for elt in elements:
        if elt is None:
            result = result + empty
        else:
            result = result + elt
    return result

def explode_list(list_of_strings): #['x..o', 'oxoo']
    result = []
    for element in list_of_strings:
        result.append(list(element))
    return result

def replace_all(matrix, old, new):
    new_matrix = []
    for element in matrix:
        new_matrix.append(replace_in_list(element, old, new))
    return new_matrix

def replace_in_list(elements, old, new):
    result = []
    for elt in elements:
        if elt == old:
            result.append(new)
        else:
            result.append(elt)
    return result