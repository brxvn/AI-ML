# Creamos un archivo coordenada.py

# La clase Coordenada guardara las coordenadas de nuestro agente
class Coordenada:

    # Definipos las coordenadas iniciales de nuestro agente   
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # dx y dy es cuanto nos estamos moviendo en cada dirección 
    # Y cuando se mueve simplemente a las coordenadas actuales se les
    # suma las coordenadas X e Y que ingresan como parámetros.
    def mover(self, dx, dy):
        return Coordenada(self.x + dx, self.y + dy)
    
    # Sólo obtenemos la distancia entre los puntos con el teorema de pitagoras alv
    def distancia(self, otra_coordenada):
        dx = self.x - otra_coordenada.x
        dy = self.y - otra_coordenada.y

        return (dx**2 + dy**2)**0.5