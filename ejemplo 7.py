print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("---------------punto 7---------------")
class Universidad():#definir las clases y sus funsiones
  def __init__(self,Nombre):
    self.Nombre=Nombre

class Carerra():
  def carrera(self,especialidad):
    self.especialidad=especialidad

class Estudiante(Universidad,Carerra):
  def datos(self,nombre,edad):
    self.nombre=nombre
    self.edad=edad#lo unico nuevo aqui es que, hay 2 datos extra y pone un mensaje y ya
    print(f"El nombre del estudiante es {self.nombre}, tiene {self.edad} años, su especialidad es {self.especialidad}. Estudia en la Universidad {self.Nombre}")

un = input("Nombre de iniversidad: ")#capturar la informacion
ing = input("Nombre de la ingeneria: ")
name = input("Nombre del estudiante: ")
ede = input("Edad del estudiante: ")

persona=Estudiante(un)#mostrar en pantalla en ejemplo.
persona.carrera(ing)
persona.datos(name, ede)
print("--------------------------------------")
print("Resultado: se ve el mensaje de manera corepta.\n")
