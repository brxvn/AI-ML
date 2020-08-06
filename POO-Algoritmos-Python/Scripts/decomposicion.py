class Automovil:
    def __init__(self, modelo, marca, color, puertas, tamaño_llantas="14'"):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.puertas = puertas
        self.tamaño_llantas = tamaño_llantas
        self._estado = "en reposo"
        self._motor = Motor(cilindros=4)

    def acelerar(self, tipo="despacio"):
        if tipo == "rapida":
            self._motor.inyecta_gas(10)
        else:
            self._motor.inyecta_gas(3)

class Motor:
    def __init__(self, cilindros, tipo="gasolina"):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gas(self, cantidad):
        pass
