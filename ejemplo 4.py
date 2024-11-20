print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("---------------punto 4---------------")
class Persona:#primera clase con funsiones
    def __init__(self, nom, ape):
        self.nombre = nom
        self.apellido = ape

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

class Estudiante(Persona):#segundo clase pero siendo clase padre de otra.
    def __init__(self, nom, ape, carr):
        super().__init__(nom, ape)
        self.carrera = carr

    def mostrar_carrera(self):
        return f"Carrera: {self.carrera}"

# Solicitar datos
nom = input("Ingrese su nombre: ")
ape = input("Ingrese su apellido: ")
carr = input("Ingrese su carrera: ")
print("----------------------------")
# Crear instancia de Estudiante
estudiante = Estudiante(nom, ape, carr)
print(estudiante.nombre_completo())
print(estudiante.mostrar_carrera())

print("--------------------------------------")
print("Resultado: las funsiones y clases son funsionaron.\n")
