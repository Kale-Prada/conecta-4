from settings import BOARD_LENGTH, VICTORY_STRIKE
from list_utils import find_strike, make_list, index_first_element

class LinearBoard:
    """
    Representamos una sola columna.
    Los jugadores son:
    - Jugador 1 : x
    - Jugador 2 : o
    - Las posiciones vacías van a ser None.

    """
    #Se usa el modificador (decorador en Python) @classmethod para indicar cuando son métodos de clase
    @classmethod
    # se suele poner "cls" para recordar que es un método de tipo self@linearboard
    def from_list(cls, data):
        """
        Me crea un linear board desde una lista
        data es una lista de listas.
        :param data:list
        :return:list
        """

        board = cls()
        #el guión bajo indica que es privada _columns, no sale fuera
        board._columns = data
        return board

    #Dunders. Cosas que yo le puedo preguntar
    #con self le indicamos que estamos en el propio board. Es exclusivo de Python
    def __init__(self):
        """
        Crea una sola columna y es como inicializamos el linear board
        """
        self._columns = make_list(BOARD_LENGTH, None)
        # [None for i in range(BOARD_LENGTH)]

    def __eq__(self, other):
        """
        Esto me sirve para poder comparar si son iguales o no las direcciones de memoria (==) entre linear boards
        :param other:
        :return:bool
        """
        #Todo lo que no sea instancia de mi propia clase = False
        if not isinstance(other, self.__class__):
            return False
        else:
            #Comparo las listas
            return self._columns == other._columns

    def __hash__(self):
        """
        No lo usamos pero es un contrato indispensable que va con __eq__.
        Sirve para ver si dos objetos comparten la misma memoria con is.
        :return:
        """
        #Hace falta convertir _columns a tupla porque una lista no en hasheable. ¡importante!
        #Esto es inamovible!
        return hash(tuple(self._columns))

    #Cosas que puede hacer
    def get_columns(self):
        """
        Obtengo la lista de una columna
        :return:
        """
        return self._columns

    def is_full(self):
        """
        Detecta si el tablero está lleno o no.
        """
        #Pregunto si el último valor es un None. Representa que al tirar la ficha me va a la última
        #posición.
        return self._columns[-1] is not None

    def add(self, char):
        """
        Se añade una ficha por cada jugador si no está lleno (comprobación previa con is_full)
        "char" es de personaje
        :param char:
        :return:
        """
        #Si no está lleno el tablero
        if not self.is_full():
            #Se usa el método "index" que busca el primer elemento. En este caso usamos una función
            # "index_first_element"
            i = index_first_element(self._columns, None)
            # i = self._column.index(None)
            self._columns[i] = char

    def is_victory(self, char):
        """
        Dice si el char(x o y) ha conseguido una racha de victory con VICTORY_STRIKE
        :param char:
        :return:
        """
        return find_strike(self._columns, char, VICTORY_STRIKE)

    def is_tie(self, char_1, char_2):
        """
        Detecta si ha sido un empate de los dos jugadores "char_1" y "char_2"
        :param char_1:
        :param char_2:
        :return:bool
        """
        #Cuando no haya victoria de char_1 y char_2 es empate. No hace falta llegar a que
        #el tablero esté lleno.
        return ((self.is_victory(char_1) == False) and
                (self.is_victory(char_2) == False))

    #Si tuviese que asignar directamente "x" y "o" sería:
    #return ((self.is_victory('x') == False) and
    #        (self.is_victory('o') == False))











