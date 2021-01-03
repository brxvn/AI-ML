class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperatura=20):
        self._llenar_tanque(temperatura)
        self._jabon()
        self._lavar()
        self._centrifugar()
    
    def _llenar_tanque(self, temperatura):
        print(f"Llenando el tanque con agua a {temperatura} grados")
    
    def _jabon(self):
        print("Añadiendo jabón")
    
    def _lavar(self):
        print("Lavando la ropa")

    def _centrifugar(self):
        print("Centrifugando")

if __name__ == "__main__":
    lavadora = Lavadora()
    lavadora.lavar()
