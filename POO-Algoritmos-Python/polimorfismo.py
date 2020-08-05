class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print("Caminando")
    

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print("Moviendome en bici")

def main():
    persona = Persona("Bryan")
    persona.avanza()
    
    ciclista = Ciclista("Daniel")
    ciclista.avanza()

if __name__ == "__main__":
    main()
