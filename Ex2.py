#Menú i estructura main
def main():
    """Mostra el menú i crida les funcions segons l'opció triada."""
    opcio = -1
    while opcio != 0:  # repite hasta elegir cero
        print()
        print("     Funcions 2")
        print("====================")
        print("1. Comptar majúscules i minúscules")
        print("2. Any de traspàs")
        print("3. Dies del mes")
        print("4. Número perfecte")
        print("5. Números perfectes fins a 10000  (repte)")
        print("0. Sortir")
        opcio = introduir_int_segur("Escull una opció: ", 0, 5)  # opcion entre cero y cinco

        if opcio == 1:
            text = input("Introdueix un text: ")
            resultat = comptar_majuscules_minuscules(text)  # guarda la tupla devuelta
            print("Majúscules:", resultat[0])
            print("Minúscules:", resultat[1])
        elif opcio == 2:
            any_usu = introduir_int_segur("Any: ", 1)  # solo comprueba el minimo
            if es_any_traspas(any_usu):  # llama funcion booleana
                print("El", any_usu, "és un any de traspàs.")
            else:
                print("El", any_usu, "no és un any de traspàs.")
        elif opcio == 3:
            mes = introduir_int_segur("Mes (1-12): ", 1, 12)  # limites minimo y maximo
            any_usu = introduir_int_segur("Any: ", 1)
            dies = comptar_dies_mes(mes, any_usu)  # funcion recibe mes y ano
            print("El mes", mes, "de l'any", any_usu, "té", dies, "dies.")
        elif opcio == 4:
            numero = introduir_int_segur("Número: ", 1)
            if es_num_perfecte(numero):
                print("El", numero, "és un número perfecte.")
            else:
                print("El", numero, "no és un número perfecte.")
        elif opcio == 5:
            print("Números perfectes fins a 10000:")
            for n in range(1, 10001):  # prueba cada numero hasta
                if es_num_perfecte(n):
                    print(n)
        else:
            print("Adéu!")

#Exercici 1. Entrada segura d'enters
def introduir_int_segur(missatge, minim=None, maxim=None):
    """
    Demana a l'usuari un número enter de forma segura.

    Args:
        missatge (str): Text a mostrar a l'usuari
        minim (int, opcional): Valor mínim acceptat
        maxim (int, opcional): Valor màxim acceptat

    Returns:
        int: Número enter vàlid introduït per l'usuari

    Exemple:
        >>> introduir_int_segur("Introdueix la teva edat: ", 0, 120)
        Introdueix la teva edat: 25
        25
    """
    correcte = False  # bandera de control bucle
    while not correcte:
        valor = input(missatge)
        if not valor.isdigit():  # comprueba solo digitos
            print("Has d'introduir un número enter.")
        elif minim is not None and int(valor) < minim:  # limite minimo opcional
            print("El número ha de ser més gran o igual que " + str(minim) + ".")
        elif maxim is not None and int(valor) > maxim:  # limite maximo opcional
            print("El número ha de ser més petit o igual que " + str(maxim) + ".")
        else:
            correcte = True
    return int(valor)  # devuelve ya convertido


#Exercici 2. Comptador de majúscules i minúscules
def comptar_majuscules_minuscules(cadena):
    """
    Compta les lletres majúscules i minúscules d'una cadena.

    Args:
        cadena (str): Cadena de text a analitzar

    Returns:
        tuple: (majúscules, minúscules)

    Exemple:
        >>> comptar_majuscules_minuscules('Una Cadena De Prova')
        (4, 12)
    """
    majuscules = 0
    minuscules = 0
    for lletra in cadena:  # recorre letra por letra
        if lletra.isupper():  # contamos cada mayuscula
            majuscules += 1
        elif lletra.islower():  # contamos cada minuscula
            minuscules += 1
    return (majuscules, minuscules)  # devuelve tupla con ambos


#Exercici 3. Any de traspàs
def es_any_traspas(a):
    """
    Determina si un any és de traspàs.

    Regles:
    - Divisible per 4, però no per 100,
    - excepte si és divisible per 400.

    Args:
        a (int): Any a comprovar

    Returns:
        bool: True si és any de traspàs, False en cas contrari

    Exemples:
        >>> es_any_traspas(2000)
        True
        >>> es_any_traspas(1900)
        False
        >>> es_any_traspas(2024)
        True
    """
    return (a % 4 == 0 and a % 100 != 0) or a % 400 == 0  # aplica regla de traspaso


#Exercici 4. Dies del mes
def comptar_dies_mes(mes, a):
    """
    Retorna el nombre de dies d'un mes en un any determinat.

    Args:
        mes (int): Número del mes (1-12)
        a (int): Any a considerar

    Returns:
        int: Nombre de dies del mes

    Exemples:
        >>> comptar_dies_mes(2, 2024)   # Febrer en any de traspàs
        29
        >>> comptar_dies_mes(2, 2023)   # Febrer en any normal
        28
        >>> comptar_dies_mes(4, 2023)   # Abril
        30

    Nota: Utilitza la funció es_any_traspas() per al febrer.
    """
    dies_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # lista con dias mensuales
    if mes == 2 and es_any_traspas(a):  # febrero depende traspaso
        return 29
    return dies_mes[mes - 1]  # posicion empieza en cero


#Exercici 5. Números perfectes
def es_num_perfecte(numero):
    """
    Comprova si un número és perfecte.

    Un número perfecte és igual a la suma dels seus divisors
    positius propis (excloent el número mateix).

    Args:
        numero (int): Número a comprovar (enter positiu)

    Returns:
        bool: True si és perfecte, False en cas contrari

    Exemples:
        >>> es_num_perfecte(6)    # 1+2+3 = 6
        True
        >>> es_num_perfecte(28)   # 1+2+4+7+14 = 28
        True
        >>> es_num_perfecte(12)
        False
    """
    suma = 0
    for i in range(1, numero // 2 + 1):  # divisores hasta la mitad
        if numero % i == 0:  # comprueba si es divisor
            suma += i
    return suma == numero  # compara suma con numero


if __name__ == "__main__":  # arranca el programa main
    main()