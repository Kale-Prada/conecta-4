import pytest

from linear_board import *
from settings import VICTORY_STRIKE, BOARD_LENGTH

def test_empty_board():

    #LinearBoard() crea un tablero que es del tipo LineaBoard que se inicializa con todo en None y tendrá los métodos
    #__init__ __eq__ y __hash__
    empty = LinearBoard()
    assert empty is not None
    assert empty.is_full() == False
    assert empty.is_victory('x') == False

def test_add():
    #Verificar si se ha metido una ficha
    b = LinearBoard()
    for i in range(BOARD_LENGTH):
        b.add('x')
    assert b.is_full() == True

def test_victory():
    b = LinearBoard()
    for i in range(VICTORY_STRIKE):
        b.add('x')
    assert b.is_victory('o') == False
    assert b.is_victory('x') == True

def test_tie():
    b = LinearBoard()

    b.add('o')
    b.add('o')
    b.add('x')
    b.add('o')

    assert b.is_tie ('x', 'o')

def test_add_to_full():
    full = LinearBoard()
    for i in range (BOARD_LENGTH):
        full.add('x')
    assert full.is_full


