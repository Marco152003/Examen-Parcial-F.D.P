#Diseña un algoritmo en el que se ingrese 2 digitos para restarlos y el programa los contabilice y los acumule usando el while.
#Declaración de las variables
acu=0
cont=0
resta=0
#Entrada
#Proceso 
#Salida
rpta = "si"
while (rpta != "no"):
    num1=int(input("Ingrese el primer digito -> "))
    num2=int(input("Ingrese el segundo digito -> "))
    acu = acu + num1 + num2
    cont = cont + 2
    resta = num1 - num2
    print("La resta es ",resta)
    print("La acumulación es ",acu)
    print("Contador de cuantos digitos ingreso ",cont)

    rpta = str (input("Desea realizar de nuevo una resta? si/no : "))