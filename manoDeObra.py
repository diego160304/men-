costos_mano_obra = {
    "Alquiler de Equipos de Topografía": 480929.12,
    "Moldero (Construcción)": 100000.00,
    "Peon": 649400.00,
    "Ayudante especializado": 587090.00,
    "Ayudante General": 570600.00,
    "Oficial albañil": 607180.00,
    "Técnico Especializado": 600239.00,
    "Oficial Tubero": 700730.00,
    "Mando Intermedio": 978730.00,
    "Topografo": 1500230.00,
    "Oficial fierrero": 975920.00,
    "Oficial carpintero de obra Negra": 800730.00,
    "Oficial pintor": 500019.00,
    "Oficial Herrero": 800920.00,
    "Oficial Yesero": 800180.00,
    "Oficial Azulejero": 750188.00,
    "Oficial colocador": 780220.00,
    "Oficial Barnizador": 800222.00,
    "Oficial Vidriero": 889019.00,
    "Maniobrista": 693140.00,
    "Oficial carpintero de obra blanca": 778730.00,
    "Oficial Aluminero": 778730.00,
    "Cabo de Oficios": 1200730.00,
    "Oficial Plomero": 978730.00,
    "Oficial Electricista": 978730.00,
    "Oficial de instalaciones": 789750.00,
    "Oficial soldador": 954750.00
}

presupuesto_total = 0.0
opcion = ""

while opcion != "3":
    print("\nMenú de Mano de Obra")
    print("1. Agregar mano de obra")
    print("2. Ver presupuesto total")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        subopcion = ""
        while subopcion != "0":
            print("\nSeleccione el tipo de mano de obra:")
            index = 1
            for rol in costos_mano_obra:
                print(f"{index}. {rol}")
                index += 1
            print("0. Volver al menú principal")
            subopcion = input("Seleccione una opción: ")

            if subopcion != "0":
                subopcion_int = int(subopcion)
                if 1 <= subopcion_int <= len(costos_mano_obra):
                    rol_seleccionado = list(costos_mano_obra)[subopcion_int - 1]
                    print(f"Seleccionado: {rol_seleccionado}")
                    cantidad_trabajadores = int(input("Ingrese la cantidad de trabajadores: "))
                    cantidad_dias = int(input("Ingrese la cantidad de días: "))
                    costo = costos_mano_obra[rol_seleccionado] * cantidad_trabajadores * cantidad_dias
                    presupuesto_total += costo
                    print(f" {cantidad_trabajadores} trabajadores por {cantidad_dias} días de {rol_seleccionado} con un costo de ${costo:.2f}. Presupuesto total: ${presupuesto_total:.2f}")
                else:
                    print("Opción no válida. Inténtelo de nuevo.")
    elif opcion == "2":
        print(f"\nPresupuesto total de mano de obra: ${presupuesto_total:.2f}")
    elif opcion == "3":
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Inténtelo de nuevo.")