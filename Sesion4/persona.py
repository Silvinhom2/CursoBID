
class Persona1:
    pass

p = Persona1() #p es una instancia de la clase persona
#print(type(p)) 

class Persona:
    def __init__(self, nombre, apellido, edad, dui): # el constructor
        self.nombre = nombre # atributo publico
        self._apellido = apellido # atributo protegido
        self.__edad = edad # atributo privado
        self.__dui = dui # privado

    def __es_adulto(self): # es privado
        return self.__edad>=18

    def mostrar_datos(self): # publico
        print(
            f'Nombre: {self.nombre}\n '
            f'Apellido: {self._apellido}\n '
            f'Edad: {self.__edad}, Adulto: {self.__es_adulto()}\n '
            f'DUI: {self.__dui}\n '
            f'***********************'
        ) 
