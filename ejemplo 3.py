print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("---------------punto 3---------------")
class Calculadora():#hasemos una clase con barias fuciones
    def __init__(self, num1, num2):#prosesar info
        self._num1=num1
        self._num2=num2#Nota: borre esto y me di cuenta de que si es muy nesario-

    def suma(self):#los sigientes 4 son lo mismo pero hasen una diferente operasion y muestran un resultado.
        resultado=self._num1 + self._num2
        print(f"El resultado de la suma es: {self._num1} + {self._num2}= {resultado}")

    def resta(self):
        resultado=self._num1 - self._num2
        print(f"El resultado de la resta es: {self._num1} – {self._num2}= {resultado}")#aqui abia un error ya que el - no lo considero como un - sino como otro un carapter

    def division(self):
        resultado=self._num1 / self._num2#esto es mas una corepsion pero puso 2 veses // y lo coregi
        print(f"El resultado de la divisón es: {self._num1} / {self._num2}= {resultado}")

    def multiplicacion(self):
        resultado=self._num1 * self._num2
        print(f"El resultado de la multiplicación es: {self._num1} * {self._num2} = {resultado}")

print("Ingresaras 2 numeros y se sumaran, restaran, dividiran y multiplicara.")#desir indicasiones y capturar los datos.
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

operacion=Calculadora(num1, num2)#que invocamos la clase con sus operasiones.
operacion.suma()
#Nota: veras margarito el operacion sirve para desir que la clase esta conetada a la funcion, bueno es creo
operacion=Calculadora(num1, num2)
operacion.resta()

operacion=Calculadora(num1, num2)
operacion.division()

operacion=Calculadora(num1, num2)
operacion.multiplicacion()
print("-------------------------------------")
print("Resultado: Se calculo todo coreptamente.\n")
