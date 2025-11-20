#Esto es una clase llamada MyClass
class MyClass:
    x = 5

# Crear un objeto de la clase MyClass
p1 = MyClass()
print(p1.x)  # Salida: 5

# Eliminar un objeto
del p1
print("El objeto p1 ha sido eliminado.")

# Crear multiples objetos de la clase MyClass
p2 = MyClass()
p3 = MyClass()
p4 = MyClass()
print(p2.x)  # Salida: 5
print(p3.x)  # Salida: 5
print(p4.x)  # Salida: 5

# Metodo pass
class EmptyClass:
    pass
