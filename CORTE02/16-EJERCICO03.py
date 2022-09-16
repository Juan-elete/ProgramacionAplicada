## 16-EJERCICO 03 RECURSIÓN
'''
Los ejercicios son de caracter obligatorio, sin embargo no se les asignará una calificación, el objetivo de estos
es que ustedes practiquen y mejoren sus habilidades.
estos los deben subir de manera individual en su cuenta de Git
'''
'''
se les darán multiples funciones, así como la documentación correspondiente
 deben completar las tareas marcadas como TODO
'''
## DEMOSTRACIONES MATEMATICAS
# ejercicios tomados de: https://elvex.ugr.es/decsai/java/pdf/7D-Ejercicios.pdf

#TODO: Demuestre por inducción que, para todo n mayor o igual que 4, n!>2^n

#TODO: Un granjero ha comprado una pareja de conejos para criarlos y luego venderlos.
#   Si la pareja de conejos produce una nueva pareja cada mes y la nueva pareja
#   tarda un mes más en ser también productiva, ¿cuántos pares de conejos podrá
#   poner a la venta el granjero al cabo de un año?

## Ejercicio objetos.
# TODO: 1. Cree un archivo, Taller donde llevará acabo el codigo principal
#       crear una lista de vehiculos que se encuentran en el taller en ese momento que tienen asociados: fecha de entrega, costo, modelo, año y dueño
#       crear una caja donde se almacena el dinero y se lleva registro de los movimientos
#       crear una lista de empleados que tienen asociado un nombre, cargo, salario, vehiculo y documento
#       Crear una lista de clientes que tienen asociado un nombre, vehiculo y documento

caja=500000000     #Se declara la variable al inicio para tener el dinero de la caja como base (5.000.000 como base)
vehiculos = 0      #Variable contadora de vehiculos

class vehicle:
    def __init__(self, d_delivery, cost, model, year, owner):
        self.d_delivery = d_delivery
        self.cost = cost
        self.model = model
        self.year = year
        self.owner = owner

class employee:
    def __init__(self, name, position, salary, car, document):
        self.name = name
        self.position = position
        self.salary = salary
        self.car = car
        self.document = document

class client:
    def __init__(self,name, document, car):
        self.name=name
        self.document = document
        self.car = car

# TODO: 2 Ejecute sobre so codigo principal:
#       ingresar un vehiculo nuevo al taller (validar cupo)
#       Sacar un vehiculo del taller (se debe generar un pago por parte del cliente)
#       PAgar a los empleados (se debe hacer una reducción en el dinero de la caja)
#       Contrarar a una persona nueva
#       Despedir a una persona
#       Encontrar un vehiculo a partir de su dueño y determinar si está en el taller


list_car = []       # Para ingresar un nuevo vehiculo realizamos en nombre de la lista. append y como parametro el nombre de la clase y sus caracteristicas
list_car.append(vehicle('13/09/2022', '20000', 'Mustang Match 1', '1969','Samuel'))
list_car.append(vehicle('15/09/2022', '12000', 'Tesla Model y', '2020', 'negro'))
list_car.append(vehicle('06/01/2022', '33000', 'Porsche Taycan', '2022', 'Paco'))
def sacarvehiculo(sacar_v,pago):  # sacar_v = el indice del vehiculo que se desea sacar     pago = El pago que realiza el cliente
    list_car1 = list_car.pop(sacar_v)
    global caja, vehiculos
    caja+=pago
    vehiculos-=1
    return list_car1,caja,vehiculos
vehiculos += len(list_car)  # Llevar al cuenta de vehiculos que hay en el taller
print("Hay", vehiculos, "vehiculos")


def pagarempleados (sueldo):            #sueldo = El pago que se le genera al empleado
    global caja
    caja-=sueldo                        #Se le resta a la caja lo que se le paga al empleado
    return caja
list_emplo = []
list_emplo.append(employee('Carlos','secretario','200','Porsche','1003809076' ))             #Contratar una nueva persona
list_emplo.append(employee('Ana','vendedora','200','Porsche','865123' ))
list_emplo.append(employee('Mauricio','limpiador de vidrios','200','Porsche','98765' ))
def despedirempleado (pa_fuera):            #pa_fuera = Es el indice del empleado que se desea despedir
    list_emplo1=list_emplo.pop(pa_fuera)
    return list_emplo1

list_client=[]
list_client.append(client('Maria','123321','Toyota'))

print(sacarvehiculo(1,200))             #Sacar el segundo vehiculo de la lista y pagar 200 por el
print(pagarempleados(300))              #Pagarle al empleado 300 y restarle este mismo valor a la caja
print(despedirempleado(1))              #Despedir al empleado del indice 1

# TODO: 3 Todas las funciones que implemente deben estar en un script distinto al principal y donde se definen sus clases
#       NOTA - (la UNICA exepción son las funciones que definen dentro de sus clases.)



