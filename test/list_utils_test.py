import pytest
from list_utils import *

def test_find_n():
    #el pajar, la aguja y la cantidad de veces que está la aguja

    #Qué ocurre si el usuario introduce un número negativo, para número de ocurrencias?
    assert find_n([2, 3, 4, 5, 6], 2, -1) == False
    #Cuando no está la aguja
    assert find_n([1, 2, 3, 4, 5], 42, 2) == False
    #El 1 aparece dos veces? no, aparece solo una = False
    assert find_n([1, 2, 3, 4, 5], 2, 2) == False
    #¿El 2 aparece dos veces? sí, aunque no estén seguidos
    assert find_n([1, 2, 3, 2, 4, 5], 2, 2)
    #El 4 está dos veces ? True
    assert find_n([1, 2, 3, 4, 5, 4, 6, 4, 7, 4, 6], 4, 2)
    #Caso que comprueba si aparece cero veces (no está) "X", Debe ser True
    assert find_n([1, 2, 3, 4],'x' , 0)

def test_find_one():
    assert find_one([1, 2, 3, 4], 1)
    assert find_one([1, 2, 3, 4], 5) == False
    assert find_one([1, 2, 3, 4], 4)
    assert find_one([4, 4, 4, 4], 4)

def test_find_one_v2():
    needle = 1
    none = [0, 0, 5, 's']
    beginning = [1, None, 9, 6, 0, 0]
    end = ['x', '0', 1]
    several = [0, 0 ,3, 4, 1, 3, 2, 1, 3, 4]

    assert find_one(none, needle) == False
    assert find_one(beginning, needle)
    assert find_one(end, needle)
    assert find_one(several, needle)


def test_find_strike():
    #¿Aparece tres veces el uno? Falso. Sólo aparece una vez.
    assert find_strike([1, 2, 3, 4], 1, 3) == False
    # ¿El 1 aparece tres veces? True (aparece al principio)
    assert find_strike([1, 1, 1, 4], 1, 3)
    #¿El 1 aparece tres veces? True (aparece al final)
    assert find_strike([2, 1, 1, 1], 1, 3)
    #No tiene sentido pedir una racha "streak" de un número negativo.
    assert find_strike([1, 2, 3, 4], 1, -3) == False
    #¿Aparece el 5 tres veces?  False. No aparece en la lista.
    assert find_strike([1, 2, 3, 4], 5, 3) == False
    #Aparece el 1 tres veces seguidas? False. Sí que hay tres unos pero no están seguidos, no hay racha.
    assert find_strike([1, 1, 3, 1], 1, 3) == False

def test_make_list():
    """Comprueba que al se longitud = 4 se rellenen los espacios vacíos con None"""
    assert make_list(4, None) == [None, None, None, None]

def test_index_first_element():
    assert index_first_element([1, 2, 3], 1) == 0
    assert index_first_element([1, 2, 3], 4) is None
