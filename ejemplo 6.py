print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("---------------punto 6---------------")
class Marino():#aqui se hase una clase padre que le dara "vida" a las demas clases
  def hablar(self):#definir
    print("Hola soy un animal marino!")#mensaje

class Pulpo(Marino):
  def hablar(self):#igual en las otras 2
    print("Hola soy un pulpo!")

class Foca(Marino):
  def hablar(self,mensaje):
    self.mensaje=mensaje
    print(mensaje)

class ani(Marino):#este es mi ejemplo
 def hablar(self,ani,mensaje):
  self.ani=ani #definir dato 1
  self.mensaje=mensaje #definir dato 2
  print("hola soy un",ani,"\nMensaje: ",mensaje) #mensaje

marino=Marino()
marino.hablar()

pulpo=Pulpo()
pulpo.hablar()

foca=Foca()
foca.hablar("Hola soy una foca!")

#capturar datos
an=input("Di un animal mario: ")
n=input("Di un mensaje de ese animal mario: ")

print("------------------------------")

pulpo=ani()#invocar clase
pulpo.hablar(an,n)#invocar funsion y alladir los datos caturados

print("--------------------------------------")
print("Resultado: el mensaje fue resivido de manera corepta.\n")
