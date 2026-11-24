from datetime import date  # Importamos date para obtener el año actual del sistema 

#Menu
def mostrar_menu():  
    """Muestra por pantalla el título y las cinco opciones del menú principal."""
    print("     Funcions 1")  # Título del menú 
    print("====================")  
    print("1. Multiplica")  # Primera opción del menú
    print("2. Anys 2000")  # Segunda opción
    print("3. Gira del revés")  # Tercera opción
    print("4. Triangle de Pascal")  # Cuarta opción
    print("5. Sortir")  # Quinta opción


#Estructura Main
def main():  
    """Muestra el menú en bucle y ejecuta la opción elegida hasta que el usuario pulse 5."""
    opcio = 0
    while opcio != 5:  # Repetimos el menu mientras no elija la opción cinco
        mostrar_menu()  # Muestra el menú completo en cada vuelta del bucle
        try:
            opcio = int(input("Escull una opció: "))  # Pedimos la opción y la convertimos a número entero
        except ValueError:
            opcio = 0  # opción en cero, mostrara el mensaje de error
        if opcio == 1:  # opción uno, pedimos los dos números y llamamos a multiplicar
            text_a = "Primer número: "
            a = None
            while a is None:  # Repetimos la petición mientras el primer número siga sin ser un entero válido
                try:
                    a = int(input(text_a))  # Pedimos el primer número y lo convertimos a entero
                except ValueError:
                    text_a = "Ha de ser un enter. Primer número: "
            text_b = "Segon número: "  
            b = None  
            while b is None:  # Repetimos la petición mientras el segundo número siga sin ser un entero válido
                try:
                    b = int(input(text_b))  # Pedimos el segundo número y lo convertimos a entero
                except ValueError:
                    text_b = "Ha de ser un enter. Segon número: "
            multiplica(a, b)  # Llamamos a la función pasándole los dos números ya validados como argumentos
        elif opcio == 2:  # opción dos, función de los años desde el 2000
            anys_2000()
        elif opcio == 3:  # opción tres, función que gira una cadena
            gira_reves()    
        elif opcio == 4:  # opción cuatro, función del triángulo de Pascal
            triangle_pascal()
        elif opcio != 5:  # Si no es ninguna opción conocida ni la de salir, es incorrecta
            print("Opció incorrecta. Ha de ser un número de l'1 al 5.")  

#1. multiplica(a, b)
def multiplica(a, b):
    """Recibe dos números enteros y muestra por pantalla el resultado de multiplicarlos"""
    print(f"{a} x {b} = {a * b}")  # Imprimimos la operación completa con el resultado

#2. anys_2000()
def anys_2000(): 
    """Pide un año entre 2000 y el año actual y muestra cuántos años han pasado desde el 2000."""
    any_actual = date.today().year
    any_usuari = 0
    valid = False  # Se usa una booleana que indica si el año escrito ya es correcto o no
    while not valid:  # Repetimos la petición mientras siga en falso
        try:
            any_usuari = int(input(f"Introdueix un any entre 2000 i {any_actual}: "))  # Lo convertimos a entero
            if 2000 <= any_usuari <= any_actual:  # comprobamos el range entre 2000 y el año actual
                valid = True
            else:
                print(f"L'any ha de ser un número entre 2000 i {any_actual}.") 
        except ValueError:  # Si el usuario escribe letras python lanza este error
            print(f"L'any ha de ser un número entre 2000 i {any_actual}.")
    print(f"Des del 2000 han passat {any_usuari - 2000} anys")  # Mostramos los años que han pasado

#3. gira_reves() 
def gira_reves():  
    """Pide una cadena y la muestra girada del revés usando solo bucles y concatenación con +."""
    c = input("Introdueix una cadena: ")
    g = ""
    for lletra in c:  # Recorremos la cadena carácter por carácter
        g = lletra + g  # Añadimos cada letra delante de lo acumulado asi el orden queda invertido
    print(g)

#4. triangle_pascal()
def triangle_pascal(): 
    """Pide un número de filas entre 2 y 10 y muestra esas filas del triángulo de Pascal."""
    n = 0 
    valid = False  # Usamos una bandera que indica si el numero de filas
    while not valid:  # Repetimos la petición si falla
        try:
            n = int(input("Nombre de files (entre 2 i 10): "))  # Pedimos las filas y las convertimos a entero
            if 2 <= n <= 10:  # Comprobamos rango del numero de 2 al 10
                valid = True
            else:
                print("Ha de ser un número entre 2 i 10.")
        except ValueError:  # Si se escribe texto que no es un número da como resultado Error
            print("Ha de ser un número entre 2 i 10.")
    fila = [1]  # Empezamos con la primera fila del triangulo
    for i in range(n):
        print(" " * (n - 1 - i), end="")  # Escribimos los espacios de la izquierda
        print(*fila)  # Mostramos los números de la fila separados por un espacio
        nova = [1]
        for j in range(len(fila) - 1):
            nova.append(fila[j] + fila[j + 1])  # Sumamos los dos números de arriba y añadimos el resultado a la nueva fila
        nova.append(1)  # Cerramos la fila nueva con un uno al final
        fila = nova  # Sustituimos la fila actual por la nueva fila

            
if __name__ == "__main__":  # punto de inicio
    main()  # Arrancamos el programa completo