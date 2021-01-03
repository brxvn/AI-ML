class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    

class Cuadrado(Rectangulo): #Al momento de definir la clase entre () le ponemos la super clase
    def __init__(self, lado): #es lo mismo que cuando en java o c# ponemos el extends y la otra clase
        super().__init__(lado, lado) #super() nos permite obtener una referencia directa de la superclase

if __name__ == "__main__":
    rectangulo = Rectangulo(3,4)
    print(rectangulo.area())
    print("hola mundo, just a test")

    cuadrado = Cuadrado(5)
    print(cuadrado.area())
