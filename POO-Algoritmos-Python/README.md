<div align="center">
  <h1>Programación orientada a objetos y Algoritmos con Python</h1>
</div>

<div align="center"> 
  <img src="readme_imgs/python_logo" width="250">
</div>

# Programación Orientada a Objetos
### Definición de clase

<pre><code>class &ltnombre_de_la_clase&gt (&ltsuper_clase&gt):

	def __init__(self, &ltparams&gt):
		&ltexpresion&gt

	def  &ltnombre_del_metodo&gt (self, &ltparams&gt):
		&ltexpresion&gt</code>
</pre>

Pueden exitir variables publicas y privadas en las clases y en los métodos. Sólo aplica para las variables y metodos en una clase (creo).

**Declaracion de una variable privada:**
Se ocupa un guion bajo antes del nombre de la variable para decir que es privada `_nombre_variable`

 **Declaracion de un método privado:** 
Ocupamos el mismo concepto de las variables privadas y lo aplicamos a los métodos, por ejemplo: `def _mi_metodo_privado()`

Ejemplo de un método privado y una variable privada:
```python
def _nombre_del_metodo_privado(self):
	self._variable_privada = True
```
Podemos llamar 2 metodos con el mismo nombre siempre y cuando sea uno privado y el otro público asi ` def _un_metodo` y `def un_metodo` pueden ser dos métodos completamente diferentes.

### Abstracción
- Enfocarnos en información relevante.
- Separar la información central de los detalles secundarios.

### Encapsulación
Programacion defensiva para determinar cuando y como se modifica una clase.
- Permite agrupar datos y su comportamiento.
- Controla el acceso a dichos datos.
- Previene modificaciones no autorizadas.

### Getters and Setters
El `@property` decorator nos permite definir un método al cual podemos acceder como si fuera un atributo o sea, podemoa acceder a el con el . (punto)

**Ejemplo:**
```python
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property   
    def email(self):#este metodo gracias al property maneja los datos mandados de emp_1
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter 
    def fullname(self, name): #este metodo es llamado en emp_1.fullname ya que le mandamos parametros para ser ocupados (setter)
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter 
    def fullname(self): #este metodo es llamado en emp_1.fullname
        print('delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('Bryan', 'Gonzalez') #de esta manera entra a la clase y solo realiza los metodos de email y fullname xq son getters
emp_1.fullname = "Pedo Gomez" #lo mandamos al setter de fullname y actualiza las variables de fiirst y last
del emp_1.fullname #nos vamos al fullname.deleter
```
Teniendo este código como ejemplo, podemos ver el `@property` decorator funcionando como un getter para el **fullname** y **email**

Para crear un setter tenemos que ocupar el `@[nombre_getter].setter` decorator.

Para cada setter tiene que haber cun getter llamado de la misma manera, por ejemplo:
```python
@property
def fullname(self):
    return f"{self.first} {self.last}"

@fullname.setter 
def fullname(self, name):
    first, last = name.split(" ")
    self.first = first
    self.last = last
```
En esta parte del código podemos ver que del el setter y el getter se llaman igual.

### Herencia
- Permite modelar una jerarquia de clases
- Permite compartir comportamiento común en la jerarquia
- Al padre se le conoce como **SuperClase** y al hijo como **subclase**

**Ejemplo:**

La manera en que la herencia funciona en python es la siguiente:
```python
class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
class Cuadrado(Rectangulo): #Al momento de definir la clase entre () le ponemos la super clase
    def __init__(self, lado): #es lo mismo que cuando en java o c# ponemos el extends y la otra clase
        super().__init__(lado, lado) #super() nos permite obtener una referencia directa de la superclase
```
`super().__init__(lado, lado)` en esta linea de código con `super()` logramos entrar al constructor de la clase **Rectangulo** pasandole los parámetro que necesita y asi poder hacer todo lo que esa clase puede hacer

### Polimorfismo
- La habilidad de tomar varias formas
- En python, nos permite cambiar el comportamiento de una superclase para adaptarlo a la subclase

**La mayor diferencia entre polimorfismo y herencia** es que el primeo busca cambiar el comportamiento de la super clase en la subclase, mientras que en la herencia solo se busca usar la estructura y comportamiento de la superclase en una subclase.

# Complejidad Algorítmica
Complejidad Temporal, es una funcion T(n) y determina el tiempo que el algoritmo tarda

### Crecimiento Asintótico
- No importan las variaciones pequeñas
- El enfoque se centra en lo suq pasa conforme el tamaño del problema se acerca al infinito.
- Mejor de los casos, promedio, peor de los casos
- Big O
- Nada mas importa el término de mayor tamaño

En Big O lo único que importa es el término mas grande sin importar el coeficiente

##### Ley de la suma
```python
def f(n):

    for i in range(n):
        print(i)
    
    for i in range(n):
        print(i)

# O(n) + O(n) = O(n + n) = O(2n) = O(n)

# CRECIMIENTO LINEAL

# La funcion crece en O(n)   
```
```python
def f(n):

    for i in range(n):
        print(i)
    
    for i in range(n * n):
        print(i)

# O(n) + O(n * n) = O(n + n²) = O(n²)

# FUNCION CUADRATICA  
```
#### Ley de la multiplicacion
```python
#Cuando se tiene un loop dentro de otro loop las variables se multiplican

def f(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

# O(n) * O(n) = O(n * n) = O(n²)
```
#### Recursividad multiple
```python
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

#O(2^n)
```