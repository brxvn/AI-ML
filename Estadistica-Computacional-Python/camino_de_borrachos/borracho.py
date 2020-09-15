# Creamos un archivo borracho.py
import random

class Borracho:

    def __init__(self, name):
        self.name = name

    
# Creamos la clase BorrachoTradicional que extiende de Borracho.
class BorrachoTradicional(Borracho):

    def __init__ (self, name):
        super().__init__(name)
    
    # Método que decide la dirección a la que irá 
    def camina(self):
        # Con random.choice elegimos un elemento aleatoriamente de la lista.
        return random.choice([ (0, 1), (0, -1), (1, 0),(-1, 0) ])