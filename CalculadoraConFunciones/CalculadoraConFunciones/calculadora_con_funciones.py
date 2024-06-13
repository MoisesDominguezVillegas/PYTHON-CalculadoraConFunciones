# Reto Calculadora con funciones
print('*** Calculadora con funciones ***')

def mostrar_menu():
    print('''Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir
    ''')
    opcion = int(input('Escoje una opcion: '))
    return opcion

def pedir_valores():
    operando1 = float(input('Escoja un primer valor: '))
    operando2 = float(input('Escoja un segundo valor: '))
    return operando1, operando2

def ejecutar_operacion(opcion, salir):
    #Solicitamos en primer lugar los operandos

        if 1 <= opcion <= 4:
            operando1, operando2 =  pedir_valores()
        resultado = 0
        if opcion == 1: # Suma
            resultado = operando1 + operando2
            print(f'El resultado de la suma es: {resultado}')
        elif opcion == 2: # Resta
            resultado = operando1 - operando2
            print(f'El resultado de la resta es: {resultado}')
        elif opcion == 3: # Multiplicacion
            resultado = operando1 * operando2
            print(f'El resultado de la mutiplicacion es: {resultado}')
        elif opcion == 4: # Division
            resultado = operando1 / operando2
            print(f'El resultado de la division es: {resultado}')
        elif opcion == 5: # Salir
            print(f'Hasta pronto!!!')
            salir= True
        else:
            print(f'Opcion invalida, escoja una opcion correcta por favor! ')
        return salir


# Codigo Principal
salir = False
while not salir:
    opcion = mostrar_menu()
    salir = ejecutar_operacion(opcion, salir)