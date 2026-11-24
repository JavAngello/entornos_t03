import random 

#1.1 DATOS DE PARTIDA

dies = ("Dilluns", "Dimarts", "Dimecres", "Dijous", "Divendres", "Dissabte", "Diumenge")  # Tupla con los 7 dias.

ciutats_catalanes = [ # Lista de las 25 ciudades.
    "Barcelona", "Girona", "Lleida", "Tarragona", "Badalona",
    "Sabadell", "Terrassa", "Mataró", "Reus", "Vic",
    "Manresa", "Granollers", "Figueres", "Olot", "Blanes",
    "Cerdanyola del Vallès", "Esplugues de Llobregat", "Gavà",
    "Sant Feliu de Llobregat", "Vilafranca del Penedès",
    "El Prat de Llobregat", "Vilanova i la Geltrú", "Cambrils",
    "Castelldefels", "L'Hospitalet de Llobregat"
]

precipitacions_possibles = [0, 0, 5, 10, 15, 20, 0, 0, 0, 0, 5, 0,  # precipitaciones posibles, el 0 se repite mucho.
                            0, 0, 10, 0, 0, 0, 0, 0, 5, 0, 0, 0] 

#1.2 GENERACIÓN DE DATOS

dades_meteorologiques = [
    { 
        "ciutat": nom_ciutat,  # Guardamos el nombre de la ciudad actual.
        "temperatures": [random.randint(5, 25) for dia in dies],  # temperaturas enteras entre 5 y 25.
        "precipitacions": [random.choice(precipitacions_possibles) for dia in dies],  # precipitaciones elegidas al azar.
        "humitat": [random.randint(40, 80) for dia in dies]  # humedades enteras entre 40 y 80.
    } 
    for nom_ciutat in ciutats_catalanes  # Repetimos para cada una de las 25 ciudades.
]  # Añadimos el diccionario a la lista general.

#1.3 MOSTRAR LA TABLA

print(f"{'Ciutat':<27}{'Temperatures (ºC)':<30}{'Precipitacions (mm)':<30}{'Humitat (%)'}")  # Cabecera con columnas de ancho fijo.
print("--------------------------------------------------------------------------------------------------------------")
for dades in dades_meteorologiques:  # Recorremos los datos de cada ciudad.
    text_temperatures = str(dades["temperatures"])[1:-1] 
    text_precipitacions = str(dades["precipitacions"])[1:-1]
    text_humitat = str(dades["humitat"])[1:-1]
    print(f"{dades['ciutat']:<27}{text_temperatures:<30}{text_precipitacions:<30}{text_humitat}")  # Fila con columnas alineadas.


#OPCIÓN 7. DICCIONARIOS DE CONJUNTOS    

pluja_per_dia = {} 
for p in range(7):  # Recorremos los 7 días por su posición.
    c_pluja = set()  # Conjunto vacío para las ciudades de este día.
    for dades in dades_meteorologiques:  # Miramos cada ciudad.
        if dades["precipitacions"][p] > 0:  # Si ese día llovió en la ciudad.
            c_pluja.add(dades["ciutat"])  # Añadimos la ciudad al conjunto.
    pluja_per_dia[dies[p]] = c_pluja  # Guardamos el conjunto con el nombre del día.

pluja_per_ciutat = {}
for dades in dades_meteorologiques:  # Recorremos cada ciudad.
    d_pluja = set()  # Conjunto vacío para los días de esta ciudad.
    for p in range(7):
        if dades["precipitacions"][p] > 0:  # Si ese día llovió en la ciudad.
            d_pluja.add(dies[p])  # Añadimos el día al conjunto.
    pluja_per_ciutat[dades["ciutat"]] = d_pluja  # Guardamos en el conjunto.


#PARTE 2: APLICACION

opcio = -1  # Valor inicial distinto de 0 para entrar al bucle.
while opcio != 0:  # Repetimos el menú hasta que elijan 0.
    print("\nAplicació meteo-DAW")
    print("=============================================") 
    print("0 Sortir") 
    print("1 Mitjana de temperatures per ciutat")
    print("2 Ciutats amb precipitació màxima")
    print("3 Dia de la setmana més calorós")
    print("4 Ordenació de ciutats per temperatura mitjana (ascendent)")
    print("5 Cerca dicotòmica de ciutat per nom")
    print("6 Freqüència de temperatures i gràfic")
    print("7 Consultes de precipitacions amb conjunts")
    print("8 Màxim, mínim i mitjana d'humitat")
    print("9 Ciutats amb temperatures sup a un llindar")
    print("10 Comparar temperatures entre dues ciutats")
    t_opcio = input("Escull una de les opcions: ").strip()  # Leemos la opción sin espacios sobrantes.
    while not (t_opcio.isdecimal() and len(t_opcio) <= 2 and int(t_opcio) <= 10):  # Repite si no es número de 0 a 10.
        print("Opció incorrecta. Ha de ser un número entre 0 i 10.") 
        t_opcio = input("Escull una de les opcions: ").strip()  # Volvemos a pedir la opción.
    opcio = int(t_opcio)  # Ya es válido: lo convertimos a número entero.
    print() 

    #OPCIÓN 1. MEDIA DE TEMPERATURAS POR CIUDAD
    if opcio == 1: 
        print("Mitjana de temperatures per ciutat")
        print("========================================")
        for dades in dades_meteorologiques:  # Recorremos cada ciudad.
            mitjana = sum(dades["temperatures"]) / len(dades["temperatures"])  # Suma de temperaturas entre 7 días.
            print(f"{dades['ciutat']}: {mitjana:.2f} ºC")

    #OPCIÓN 2. CIUDADES CON PRECIPITACIÓN MÁXIMA
    elif opcio == 2:
        print("Ciutats amb precipitació màxima")
        print("========================================")
        totals = []  # Lista vacía para guardar el total de cada ciudad.
        for dades in dades_meteorologiques:  # Recorremos cada ciudad.
            total = sum(dades["precipitacions"])
            totals.append(total)  # Guardamos el total en la lista.
            print(f"{dades['ciutat']}: {dades['precipitacions']} - TOTAL = {total} mm")  # Mostramos precipitaciones diaria y total.
        maxim = max(totals)
        ciutats_max = []  # Lista vacía para las ciudades con el máximo.
        for i in range(len(dades_meteorologiques)):  # Recorremos las pnes de las ciudades.
            if totals[i] == maxim: 
                ciutats_max.append(dades_meteorologiques[i]["ciutat"])  # Guardamos su nombre.
        print()
        print(f"Precipitació màxima de la setmana: {maxim} mm")
        print("Ciutat/s: " + ", ".join(ciutats_max))

    #OPCIÓN 3. DÍA DE LA SEMANA MÁS CALUROSO
    elif opcio == 3: 
        print("Dia de la setmana més calorós")
        print("========================================")
        s_dia = []  # Lista vacía para la suma de temperaturas de cada día.
        for p in range(7): # Recorremos las posiciones de los 7 días.
            suma = 0  # Empezamos la suma del día en cero.
            for dades in dades_meteorologiques: 
                suma = suma + dades["temperatures"][p]  # Sumamos la temperatura de ese día.
            s_dia.append(suma)  # Guardamos la suma del día.
            print(f"{dies[p]}: {suma / len(dades_meteorologiques):.2f} ºC")  # Mostramos la media del día.
        suma_max = max(s_dia)  # La suma más alta de la semana.
        print()
        for p in range(7): 
            if s_dia[p] == suma_max:  # Si este día tiene la suma máxima.
                print(f"El dia més calorós ha estat: {dies[p]} ({suma_max / len(dades_meteorologiques):.2f} ºC de mitjana)")  # Mostramos los dias mas calurosos.

    #OPCIÓN 4 ORDENACIÓN DE CUIDADES POR TEMPERATURA MEDIA
    elif opcio == 4:
        print("Ordenació de ciutats per temperatura mitjana") 
        print("========================================")
        llista_mit = []  # Lista vacía de tuplas (ciudad, media).
        for dades in dades_meteorologiques: 
            mitjana = sum(dades["temperatures"]) / len(dades["temperatures"])  # Calculamos su temperatura media.
            llista_mit.append((dades["ciutat"], mitjana))  # Guardamos la tupla en la lista.
        print("Sense ordenar:") 
        print("----------------------------------------")
        for tupla in llista_mit:  # Recorremos las tuplas sin ordenar.
            print(f"{tupla[0]}: {tupla[1]:.2f} ºC") 
        llista_ord = llista_mit.copy()  # Copia para no cambiar la lista original.
        for ronda in range(len(llista_ord) - 1):  # Cada ronda coloca un valor grande al final.
            for j in range(len(llista_ord) - 1 - ronda):  # Comparamos parejas que aún no están fijas.
                if llista_ord[j][1] > llista_ord[j + 1][1]:
                    aux = llista_ord[j]  # Guardamos la primera tupla en una variable.
                    llista_ord[j] = llista_ord[j + 1]  # Subimos la segunda tupla a la primera posición.
                    llista_ord[j + 1] = aux  # Colocamos la primera tupla en la segunda posición.
        print()
        print("Ordenades (ascendent):")
        print("----------------------------------------")
        for tupla in llista_ord:  # Recorremos las tuplas ya ordenadas.
            print(f"{tupla[0]}: {tupla[1]:.2f} ºC") 

    #OPCIÓN 5. CERCA DICOTÒMICA DE CIUDAD POR NOMBRE
    elif opcio == 5:
        print("Cerca dicotòmica de ciutat per nom") 
        print("========================================")
        noms_ordenats = sorted(ciutats_catalanes)  # Nombres ordenados alfabéticamente1.
        t_cerca = input("Introdueix una ciutat: ").strip() 
        cerca = t_cerca.lower()  # Pasamos a minúsculas para comparar.
        izq = 0 
        dere = len(noms_ordenats) - 1 
        p_trob = -1  # El -1 significa que aún no se encontró.
        while izq <= dere and p_trob == -1:  # Seguimos mientras quede zona y no se halle.
            mig = (izq + dere) // 2  # Calculamos la posición central.
            nom_mig = noms_ordenats[mig].lower() 
            if nom_mig == cerca:  # Si el del centro es el buscado.
                p_trob = mig 
            elif nom_mig < cerca:  # Si el del centro va antes alfabéticamente.
                izq = mig + 1 
            else:  # Si el del centro va después alfabéticamente.
                dere = mig - 1 
        if p_trob != -1:  # Si la ciudad se encontró.
            print(f"La ciutat {noms_ordenats[p_trob]} es troba a la posició {p_trob + 1} de {len(noms_ordenats)}.")  # Posición contando desde 1.
        else:  # Si la ciudad no se encontró.
            print(f"La ciutat {t_cerca} no es troba a la llista.") 

    #OPCIÓN 6. FRECUENCIA DE TEMPERATURAS Y GRÁFICO
    elif opcio == 6:
        freq = []  # Lista vacía de tuplas (temperatura, veces).
        for temp in range(5, 26):  # Probamos cada temperatura de 5 a 25.
            vegades = 0 
            for dades in dades_meteorologiques: 
                vegades = vegades + dades["temperatures"].count(temp)  # Sumamos cuántas veces aparece en la ciudad.
            freq.append((temp, vegades))  # Guardamos la tupla en la lista.
            print(f"Temperatura {temp} ºC apareix {vegades} vegades") 
        max_vegades = 0
        for tupla in freq:  # Recorremos las tuplas guardadas.
            if tupla[1] > max_vegades:  # Si supera el máximo actual.
                max_vegades = tupla[1]  # Actualizamos el máximo.
        print()
        for tupla in freq:  # Buscamos todas las temperaturas empatadas.
            if tupla[1] == max_vegades:  # Si tiene el máximo de repeticiones.
                print(f"Temperatura més freqüent: {tupla[0]} ºC ({tupla[1]} vegades)")  # Mostramos la más frecuente.
        print() 
        print("Gràfic de temperatures")
        print("======================")
        for n in range(max_vegades, 0, -1):  # Filas del gráfico, de arriba hacia abajo.
            fila = f"{n:>3} |"  # La fila empieza con su número de nivel.
            for tupla in freq:  # Recorremos cada temperatura (columna).
                if tupla[1] >= n:  # Si la barra llega a este nivel.
                    fila = fila + "  #"  # Dibujamos una almohadilla.
                else: 
                    fila = fila + "   "  # Dejamos un hueco vacío.
            print(fila)
        print("    +" + "-" * 63)  # Eje horizontal del gráfico.
        l_temp = "     "  # Margen inicial para alinear los números.
        for tupla in freq:
            l_temp = l_temp + f"{tupla[0]:>3}"  # Añadimos cada temperatura con ancho 3.
        print(l_temp) # Imprimimos la línea de temperaturas.

    #OPCIÓN 7. CONSULTAS DE PRECIPITACIONES CON CONJUNTOS
    elif opcio == 7:
        print("Consultes de precipitacions amb conjunts") 
        print(("========================================"))

        #a) dos ciudades
        ciutat1 = ""  # Vacía significa que aún no hay ciudad válida.
        while ciutat1 == "":  # Pedimos hasta tener una ciudad válida.
            text = input("Introdueix la primera ciutat: ").strip()  # Leemos lo que escribe el usuario.
            for ciutat in ciutats_catalanes:  # Comparamos con cada ciudad oficial.
                if ciutat.lower() == text.lower():  # Si coincide sin mirar mayúsculas.
                    ciutat1 = ciutat  # Guardamos el nombre.
            if ciutat1 == "":  # Si no coincidió con ninguna.
                print(f"La ciutat {text} no es troba a la llista.")
        ciutat2 = ""  # Vacía significa que aún no hay segunda ciudad.
        while ciutat2 == "":  # Pedimos hasta tener una segunda ciudad válida.
            text = input("Introdueix la segona ciutat: ").strip()
            for ciutat in ciutats_catalanes:  # Comparamos con cada ciudad oficial.
                if ciutat.lower() == text.lower():  # Si coincide sin mirar mayúsculas.
                    ciutat2 = ciutat  # Guardamos el nombre.
            if ciutat2 == "":  # Si no coincidió con ninguna.
                print(f"La ciutat {text} no es troba a la llista.") 
            elif ciutat2 == ciutat1:  # Si es la misma que la primera.
                print("Has d'escollir dues ciutats diferents.") 
                ciutat2 = ""  # Lo dejamos vacio para volver a pedir.
        dies1 = pluja_per_ciutat[ciutat1]  # Días con precipitaciones en la primera ciudad.
        dies2 = pluja_per_ciutat[ciutat2]  # Días con precipitaciones en la segunda ciudad.
        print() 
        print(f"A {ciutat1} ha plogut: {dies1}")  # Días de precipitaciones de la ciudad 1.
        print(f"A {ciutat2} ha plogut: {dies2}")  # Días de precipitaciones de la ciudad 2.
        print(f"Dies que ha plogut a les dues ciutats: {dies1 & dies2}")  # Intersección.
        print(f"Dies que ha plogut a {ciutat1} però no a {ciutat2}: {dies1 - dies2}")  # Diferencia.
        print(f"Dies que ha plogut només en una de les dues: {dies1 ^ dies2}")  # Diferencia simétrica.
        print(f"Dies que ha plogut en alguna de les dues: {dies1 | dies2}")  # Unión.
        print() 

        # b) dos días
        dia1 = ""  
        while dia1 == "":  
            text = input("Introdueix un dia de la setmana: ").strip()
            for dia in dies: 
                if dia.lower() == text.lower():  # Si coincide sin mirar mayúsculas.
                    dia1 = dia  
            if dia1 == "":  # Si no coincidió con ninguno.
                print(f"El dia {text} no existeix.")
        dia2 = "" 
        while dia2 == "":  # Pedimos hasta tener un segundo día válido.
            text = input("Introdueix un dia de la setmana: ").strip()
            for dia in dies: 
                if dia.lower() == text.lower():  # Si coincide sin mirar mayúsculas.
                    dia2 = dia  
            if dia2 == "":  # Si no coincidió con ninguno.
                print(f"El dia {text} no existeix.")
            elif dia2 == dia1:  # Si es el mismo que el primero.
                print("Has d'escollir dos dies diferents.")
                dia2 = "" 
        ciutats1 = pluja_per_dia[dia1] 
        ciutats2 = pluja_per_dia[dia2]  
        print()
        print(f"El {dia1} ha plogut a: {ciutats1}")  
        print(f"El {dia2} ha plogut a: {ciutats2}") 
        print(f"Ciutats on ha plogut els dos dies: {ciutats1 & ciutats2}")  # Intersección.
        print(f"Ciutats on ha plogut el {dia1} però no el {dia2}: {ciutats1 - ciutats2}")  # Diferencia.
        todes_ciu = set(ciutats_catalanes)  # Lista de ciudades convertida en conjunto.
        print(f"Ciutats on no ha plogut cap dels dos dies: {todes_ciu - (ciutats1 | ciutats2)}")  # Todas menos las que llovió.

    #OPCIÓN 8. HUMEDAD MÁXIMA, MÍNIMA Y MEDIA
    elif opcio == 8:
        print(f"{'Ciutat':<27}{'Màxim (%)':>10}{'Mínim (%)':>11}{'Mitjana (%)':>13}")  # Cabecera de la tabla alineada.
        print("--------------------------------------------------------------")
        humitats_totes = []  # Lista vacía con todas las humedades de todas las ciudades.
        for dades in dades_meteorologiques:
            humitat_max = max(dades["humitat"]) 
            humitat_min = min(dades["humitat"]) 
            humitat_mitj = sum(dades["humitat"]) / len(dades["humitat"])  # Humedad media de la ciudad.
            print(f"{dades['ciutat']:<27}{humitat_max:>10}{humitat_min:>11}{humitat_mitj:>13.2f}")  # Fila con los tres valores.
            humitats_totes.extend(dades["humitat"])  # Añadimos sus humedades a la lista global.
        print("--------------------------------------------------------------")
        print() 
        print("Humitat global:") 
        print(f"Màxim: {max(humitats_totes)} %") 
        print(f"Mínim: {min(humitats_totes)} %")
        print(f"Mitjana: {sum(humitats_totes) / len(humitats_totes):.2f} %") 

    #OPCIÓN 9. CIUDADES Y TEMPERATURAS SUPERIORES AL UMBRAL
    elif opcio == 9:
        t_llindar = input("Introdueix un llindar (entre 5 i 25): ").strip()  # Pedimos el umbral de temperatura.
        while not (t_llindar.isdecimal() and len(t_llindar) <= 2 and 5 <= int(t_llindar) <= 25):  # Repite si no es entero de 5 a 25.
            print("Valor incorrecte.") 
            t_llindar = input("Introdueix un llindar (entre 5 i 25): ").strip()  # Volvemos a pedir el umbral.
        llindar = int(t_llindar)
        sup = [dades["ciutat"] for dades in dades_meteorologiques if max(dades["temperatures"]) > llindar]  # List comprehension de ciudades que superaron el umbral.
        print() 
        if len(sup) > 0:  # Si al menos una ciudad lo superó.
            print(f"Ciutats que han superat els {llindar} ºC algun dia ({len(sup)}):")  # Mostramos cuántas hay.
            print(", ".join(sup))  # Mostramos sus nombres separados por comas.
        else:  # Si ninguna ciudad lo superó.
            print(f"Cap ciutat ha superat els {llindar} ºC cap dia (0).")  # Avisamos de que no hay ninguna.

    #OPCIÓN 10. COMPARAR TEMPERATURAS ENTRE DOS CIUDADES
    elif opcio == 10:
        ciutat1 = ""  # Vacía significa que aún no hay ciudad válida.
        while ciutat1 == "":  # Pedimos hasta tener una ciudad válida.
            text = input("Introdueix la primera ciutat: ").strip()
            for ciutat in ciutats_catalanes:  # Comparamos con cada ciudad oficial.
                if ciutat.lower() == text.lower():  # Si coincide sin mirar mayúsculas.
                    ciutat1 = ciutat 
            if ciutat1 == "":  # Si no coincidió con ninguna.
                print(f"La ciutat {text} no es troba a la llista.")  # Avisamos del error.
        ciutat2 = ""  # Vacía significa que aún no hay segunda ciudad.
        while ciutat2 == "":  # Pedimos hasta tener una segunda ciudad válida.
            text = input("Introdueix la segona ciutat: ").strip()
            for ciutat in ciutats_catalanes:  # Comparamos con cada ciudad oficial.
                if ciutat.lower() == text.lower():  # Si coincide sin mirar mayúsculas.
                    ciutat2 = ciutat 
            if ciutat2 == "":  # Si no coincidió con ninguna.
                print(f"La ciutat {text} no es troba a la llista.")
            elif ciutat2 == ciutat1:  # Si es la misma que la primera.
                print("Has d'escollir dues ciutats diferents.") 
                ciutat2 = ""  # Vaciamos para volver a pedir.
        temp1 = []
        temp2 = []
        for dades in dades_meteorologiques:  # Recorremos los datos de todas las ciudades.
            if dades["ciutat"] == ciutat1:  # Si es la primera ciudad elegida.
                temp1 = dades["temperatures"]  # Guardamos sus temperaturas.
            if dades["ciutat"] == ciutat2:  # Si es la segunda ciudad elegida.
                temp2 = dades["temperatures"]  # Guardamos sus temperaturas.
        print() 
        print(f"{ciutat1}: {str(temp1)[1:-1]}")  
        print(f"{ciutat2}: {str(temp2)[1:-1]}") 
        print() 
        for p in range(7): 
            t1 = temp1[p]  
            t2 = temp2[p] 
            if t1 == t2:  # Si las dos temperaturas son iguales.
                print(f"{dies[p]}: a {ciutat1} i a {ciutat2} ha fet la mateixa temperatura ({t1} ºC)")
            elif t1 > t2:  # Si la ciudad 1 tuvo más calor.
                print(f"{dies[p]}: a {ciutat1} ha fet més calor que a {ciutat2} ({t1} ºC / {t2} ºC)")
            else:  # Si la ciudad 1 tuvo menos calor.
                print(f"{dies[p]}: a {ciutat1} ha fet més fred que a {ciutat2} ({t1} ºC / {t2} ºC)")

    #OPCIÓN 0. SALIR
    else: 
        print("tancar aplicació")   