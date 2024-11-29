precios_estructura = { 
    'Bloques de construcción (35 bloques)': 100000,
    'Metales reforzados (20 metros)': 200000,
    'Sacos de cemento (100 kg)': 50000,
    'Gravilla y arena (1,200 kg)': 30000,
    'Madera tratada (10 metros)': 150000
}

precios_acabado = {
    'Estuco y pintura (1 galón - 45 m²)': 50000,  
    'Cerámicas decorativas (1 caja - 2 m²)': 40000,
    'Láminas para techos (1 lámina - 2 m²)': 60000
}

costo_total = 0
materiales_elegidos = []

materiales_estructura = [
    'Bloques de construcción (35 bloques)', 
    'Metales reforzados (20 metros)', 
    'Sacos de cemento (100 kg)', 
    'Gravilla y arena (1,200 kg)', 
    'Madera tratada (10 metros)'
]
materiales_acabado = [
    'Estuco y pintura (1 galón - 45 m²)', 
    'Cerámicas decorativas (1 caja - 2 m²)', 
    'Láminas para techos (1 lámina - 2 m²)'
]

# Diccionario para almacenar la cantidad de cada material seleccionado
materiales_seleccionados = {}

while True:
    print("\nMenú principal")
    print("1. Seleccionar materiales de estructura")
    print("2. Seleccionar materiales de acabado")
    print("3. Editar presupuesto")
    print("4. Mostrar resumen y salir")
    opcion = input("Elija una opción: ")

    if opcion == '1':
        while True:
            print("\nMateriales disponibles para estructura:")
            for i, material in enumerate(materiales_estructura):
                print(f"{i+1}. {material} - Precio: ${precios_estructura[material]:,} COP")
            print("0. Volver al menú principal")

            subopcion = input("Seleccione un material o vuelva al menú: ")

            if subopcion == '0':
                print("Regresando al menú principal...")
                break
            elif subopcion in ['1', '2', '3', '4', '5']:
                material_seleccionado = materiales_estructura[int(subopcion) - 1]
                precio = precios_estructura[material_seleccionado]
                cantidad = 1  # Se asume que la cantidad inicial es 1
                costo_total += precio * cantidad
                materiales_elegidos.append(f"{material_seleccionado} x {cantidad} unidades")
                materiales_seleccionados[material_seleccionado] = cantidad
                print(f"Has agregado: {material_seleccionado}. Precio: ${precio:,} COP")
                print(f"Costo total acumulado: ${costo_total:,} COP")
            else:
                print("Opción no válida. Intente de nuevo.")

    elif opcion == '2':
        while True:
            print("\nMateriales disponibles para acabado:")
            for i, material in enumerate(materiales_acabado):
                print(f"{i+1}. {material} - Precio: ${precios_acabado[material]:,} COP")
            print("0. Volver al menú principal")

            subopcion = input("Seleccione un material o vuelva al menú: ")

            if subopcion == '0':
                print("Regresando al menú principal...")
                break
            elif subopcion in ['1', '2', '3']:
                material_seleccionado = materiales_acabado[int(subopcion) - 1]
                cantidad = int(input(f"Ingrese la cantidad de {material_seleccionado.split('(')[0].strip()}: "))
                precio_unitario = precios_acabado[material_seleccionado]
                costo_total += precio_unitario * cantidad
                materiales_elegidos.append(f"{material_seleccionado} x {cantidad} unidades")
                materiales_seleccionados[material_seleccionado] = cantidad
                print(f"Has agregado: {material_seleccionado}. Cantidad: {cantidad}. Precio total: ${precio_unitario * cantidad:,} COP")
                print(f"Costo total acumulado: ${costo_total:,} COP")
            else:
                print("Opción no válida. Intente de nuevo.")

    elif opcion == '3':
        print("\nMateriales seleccionados:")
        for i, material in enumerate(materiales_elegidos):
            print(f"{i+1}. {material}")
        
        edit_opcion = input("Seleccione el material que desea editar (ingrese el número) o 0 para volver al menú: ")
        
        if edit_opcion == '0':
            print("Regresando al menú principal...")
        elif edit_opcion in [str(i+1) for i in range(len(materiales_elegidos))]:
            material_a_editar = materiales_elegidos[int(edit_opcion) - 1]
            print(f"Has seleccionado editar: {material_a_editar}")
            
            # Recuperar el material de la lista de seleccionados (sin usar split ni pop)
            for material in materiales_seleccionados:
                if material in material_a_editar:
                    material_nombre = material
                    break
            
            precio_unitario = precios_acabado.get(material_nombre, precios_estructura.get(material_nombre))

            # Eliminar el material previo (restar del costo total)
            cantidad_anterior = materiales_seleccionados[material_nombre]
            costo_total -= precio_unitario * cantidad_anterior

            # Actualizar la cantidad
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            materiales_seleccionados[material_nombre] = nueva_cantidad
            costo_total += precio_unitario * nueva_cantidad

            # Actualizar la lista de materiales elegidos
            materiales_elegidos[int(edit_opcion) - 1] = f"{material_nombre} x {nueva_cantidad} unidades"

            print(f"Material editado: {material_nombre} x {nueva_cantidad} unidades. Precio total actualizado: ${costo_total:,} COP")
        else:
            print("Opción no válida. Intente de nuevo.")

    elif opcion == '4':
        print("\nMateriales seleccionados:")
        for material in materiales_elegidos:
            print(f"- {material}")
        
        print(f"\nEl costo total final es: ${costo_total:,} COP")
        print("Gracias por usar el sistema de selección de materiales. ¡Hasta pronto!")
        break

    else:
        print("Opción no válida. Intente de nuevo.")
