# El metodo init nos permitira inicializar los atributos de una clase. Si no usamos el metodo init tendremos 
# que crear de forma manual los atributos de cada objeto que creemos a partir de la clase.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Eduardo", 25)

print(f"Name: {person1.name}, Age: {person1.age}")

# Valores creados de forma prederterminada
class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

person2 = Person("Ana")
print(f"Name: {person2.name}, Age: {person2.age}")

#Uso del self nos permite acceder a los atributos y metodos de la clase dentro de la misma clase.
# No es necesario llamar al self, si esta en la primera posicion del metodo tendra acceso a los atributos y metodos de la clase.
class Person:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f"Name: {self.name}")

person3 = Person("Carlos")
person3.print_name()
        