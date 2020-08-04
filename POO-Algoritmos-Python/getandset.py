class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property   #este metodo gracias al property maneja los datos mandados de emp_1
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter #este metodo es llamado en emp_1.fullname ya que le mandamos parametros para ser ocupados (setter)
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter #este metodo es llamado en emp_1.fullname
    def fullname(self):
        print('delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('Bryan', 'Gonzalez') #de esta manera entra a la clase y solo realiza los metodos de email y fullname xq son getters
emp_1.fullname = "Pedo Gomez" #lo mandamos al setter de fullname y actualiza las variables de fiirst y last
del emp_1.fullname #nos vamos al fullname.deleter

print(emp_1.first)
print(emp_1.last)
print(emp_1.email)
print(emp_1.fullname)

