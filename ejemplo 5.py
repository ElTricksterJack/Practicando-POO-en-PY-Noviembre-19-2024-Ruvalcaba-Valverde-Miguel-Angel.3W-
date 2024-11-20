print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("---------------punto 5---------------")
class Fabrica():#esta es la clase de llantas, que prosesa la informasion de color, presio y llantas
  def __init__(self, llantas, color, precio):
    self._llantas=llantas
    self._color=color
    self._precio=precio

class Moto(Fabrica):#esta es la clase de moto, pero tambien usa de llantas como padre
  def cantidad(self):#definir funsion
    print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: ${}".format(self._llantas,self._color,self._precio))
    #haser que se escriba el texto, con las devidas espasios para que se bean los resultado.
    print("OBJETO=carro")

class Carro(Fabrica):#lo mismo pero con carro
  def cantidad(self):
    print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: ${}".format(self._llantas,self._color,self._precio))
    print("OBJETO=moto")

moto=Moto(2, "Gris", 200)#ejemplo con una moto
moto.cantidad()

print("*-----------------*")

print("--Para un carro--")#aqui tu hases un ejemplo, propio donde tu eliges la cantidad de llantas, color y presio.
#aunque en la vida real no funsiona hasi.
#hay me acabo de acordar de el momento en el que lucy le pone una mantita a Rip y Latla, es algo hermoso, hay que triste, recuerdo como llore cuando leei eso en el camino a a juarez.
#hay Rip y Latla, es triste no merian morir, ni ustedes ni Inchigo, Nico, Gina, Billy, Ttiana, Backs, Yuusei, y todos hay como me duele de recordar.

lla = int(input("Numero de llantas: "))
col = input("Color de llantas: ")
pri = float(input("Precio de llantas: "))
print("/-+-+-+-+-+-+-/")
carro=Carro(lla ,col, pri)#aqui invocamos la funsion y listo.
carro.cantidad()

print("--------------------------------------")
print("Resultado: Se muestran bien todo.\n")
