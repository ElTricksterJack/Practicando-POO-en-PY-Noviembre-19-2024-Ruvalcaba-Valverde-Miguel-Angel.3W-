print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("---------------punto 1---------------")
class Estudiante(): #qui definimos la clase
    def __init__(self , nom , cal): 
        self.nom=nom#aqui se inicializan los atributos
        self.cal=cal

    def imprimir(self):#aqui hasemos otra funcion, donde escriben en pantalla el nombre y calificasion del aluno
        print(f"Nombre:{self.nom} \nCalificasion: {self.cal}")

    def resultados(self):#en esta funsion se dise si el albuno parobo o no.
        if self.cal >= 7:
            print("Felizidades has pasado")
            print("----------------")
        else:
            print("Balla has reprobado")
            print("----------------")
#como tal esta es una cadena de funsiones donde hay barias funsiones entre si, muy interesante.

estudiante1=Estudiante("Morgans" , 5)
estudiante1.imprimir()
estudiante1.resultados()

estudiante2=Estudiante("Mora" , 7)
estudiante2.imprimir()
estudiante2.resultados()
#Con esto de ariba invocamos las funsiones en cadena la primera prosesa el nombre y calificasion, la segunda los escribe en pantalla y el tersero dise si paso o no
#lo de abajo es un ejemplo.
n = input("Ingrese su nombre: ")
c = float(input("ingresa tu calificasion: "))
print("---------------------------------")
estudiante3=Estudiante(n, c)
estudiante3.imprimir()
estudiante3.resultados()

print("-------------------------------------")
print("Resultado: se logro ber el numero, calificasion y dise si aprobo o no.\n")
