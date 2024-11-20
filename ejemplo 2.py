print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("---------------punto 2---------------")
class Persona:#hasemos una clase con 2 funsiones
  def __init__(self, n, e):#esta prosesa el nombre y edad
    self.nombre=n
    self.edad=e

  def cumpleaños(self):#esta suma la edad
    self.edad += 1

p=Persona(input("Ingrese nombre: "),int(input("Ingrese edad: ")))#ahora con el imput se pone a prueba
#Nota: no sabia que se podian poner 2 input, pero al pareser es muy interesante.
p.cumpleaños()
print(f"{p.nombre} cumple {p.edad} años, felizidades")
#soy yo o qui hay errores echos a proposito para que lo resolbamos?.
print("-------------------------------------")
print("Resultado: se ve el resultado y la suma se hase coreptamente.\n")
