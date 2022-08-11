## EJERCICIO 01
'''
Los ejercicios son de caracter obligatorio, sin embargo no se les asignará una calificación, el objetivo de estos
es que ustedes practiquen y mejoren sus habilidades.
estos los deben subir de manera individual en su cuenta de Git
'''
'''
se les darán multiples funciones (por ahora no importa qué son), así como la documentación correspondiente
 deben completar las tareas marcadas como TODO
'''
##
def f_suma (a,b):
    '''
    Esta funcion debe asignar el varor de la suma entre a y b a la variable a
    :param a: número
    :param b: número
    :return: suma entre a y b
    '''
    #TODO: En este espacio deben realizar las modificaciones

    return a
# Se genera un error si no funciona de manera adecuada
assert f_suma(3,5) == 8
assert f_suma(3,-5) == -2
assert f_suma(-7,-5) == -12
## modulo

def f_mod(a,b):
    '''
    asigna el modulo entre b y a
    :param a: primer numero
    :param b: segundo número
    :return: retorna el módulo entre b y a
    '''
    #TODO: En este espacio deben realizar las modificaciones

    return b

# Se genera un error si no funciona de manera adecuada
assert f_mod(3,5) == 2
assert f_mod(3,-5) == -1
assert f_mod(4,10) == 2

## Cadenas de caracteres
def f_str_01 (str_01):
    '''
    Realice una función que separe por espacio una cadena de caracteres convierte en mayusculas la segunda palabra
    y retorna la cadena unida sin espacios.
    NOTA: deben asignar la nueva cadena a la cadena a la variable str_02
    :param str_01:
    :return: str_02
    '''
    # TODO: En este espacio deben realizar las modificaciones
    return str_02

assert f_str_01('Hola Mundo') == 'HolaMUNDO'
assert f_str_01('tengo un dinosaurio') == 'tengoUNdinosaurio'


#######################################

print("Primer punto")

def f_suma (a,b):
    print(a+b)
    return(a+b)

assert f_suma(3,5) ==8
assert f_suma(3,-5) == -2
assert f_suma(-7,-5) == -12

print("Segundo punto")
def f_mod(a,b):
    print(b%a)
    return (b%a)

assert f_mod(3,5) == 2
assert f_mod(3,-5) == 1
assert f_mod(4,10) == 2

print("Tercer punto")

str_01 = "hola mundo soy chimba"
separados=(str_01.split())
print (separados)
str_02 = separados[0] + separados[1].upper()

print (str_02)

