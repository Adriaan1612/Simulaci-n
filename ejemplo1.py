#vamos a utilizar el contenido del módulo ejemplo2

import ejemplo2
from ejemplo3 import Pais

#uso de variables
ejemplo2.alumnos.update({"Luis":"dam"})
print(ejemplo2.alumnos)

#use de funciones
ejemplo2.calcular_cubo()

#uso de una clase
producto1=ejemplo2.Producto("camisa",50)

francia=Pais("Frances","Paris")