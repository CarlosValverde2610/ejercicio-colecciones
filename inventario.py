# =====================================================================
# TAREA PRÁCTICA: Colecciones de Datos en Python
# Problema: Gestión de inventario de productos para una tienda
# =====================================================================

def mostrar_menu():
    print("\n--- SISTEMA DE GESTIÓN DE INVENTARIO ---")
    print("1. Agregar producto (Diccionario / Lista)")
    print("2. Mostrar todos los productos")
    print("3. Buscar un producto por nombre")
    print("4. Eliminar un producto")
    print("5. Ver categorías únicas de productos (Conjunto)")
    print("6. Salir")

def main():
    # 1. COLECCIONES DE DATOS UTILIZADAS:
    # - Lista: Almacena los productos en orden.
    # - Diccionario: Representa cada producto con sus atributos (nombre, precio, categoría).
    # - Conjunto (Set): Almacena categorías únicas sin repetir.
    
    inventario = []
    categorias_unicas = set()

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-6): ").strip()

        if opcion == "1":
            # FUNCIONALIDAD: Agregar datos
            print("\n--- Agregar Producto ---")
            nombre = input("Nombre del producto: ").strip().capitalize()
            
            try:
                precio = float(input("Precio ($): "))
            except ValueError:
                print("Error: El precio debe ser un número válido.")
                continue

            categoria = input("Categoría: ").strip().capitalize()

            # Estructura del diccionario
            producto = {
                "nombre": nombre,
                "precio": precio,
                "categoria": categoria
            }

            # Inserción en lista y conjunto
            inventario.append(producto)
            categorias_unicas.add(categoria)
            print(f"✅ Producto '{nombre}' registrado con éxito.")

        elif opcion == "2":
            # FUNCIONALIDAD: Mostrar información (Recorrer elementos)
            print("\n--- Lista de Productos ---")
            if not inventario:
                print("El inventario está vacío.")
            else:
                for idx, prod in enumerate(inventario, start=1):
                    print(f"{idx}. Producto: {prod['nombre']} | Precio: ${prod['precio']:.2f} | Categoría: {prod['categoria']}")

        elif opcion == "3":
            # FUNCIONALIDAD: Operación adicional - Buscar
            print("\n--- Buscar Producto ---")
            busqueda = input("Ingrese el nombre del producto a buscar: ").strip().capitalize()
            encontrado = False

            for prod in inventario:
                if prod["nombre"] == busqueda:
                    print(f"🔍 Encontrado: {prod['nombre']} - Precio: ${prod['precio']:.2f} - Categoría: {prod['categoria']}")
                    encontrado = True
                    break
            
            if not encontrado:
                print(f"❌ El producto '{busqueda}' no se encuentra en el inventario.")

        elif opcion == "4":
            # FUNCIONALIDAD: Operación adicional - Eliminar
            print("\n--- Eliminar Producto ---")
            eliminar_nombre = input("Ingrese el nombre del producto a eliminar: ").strip().capitalize()
            inicial_len = len(inventario)

            inventario = [prod for prod in inventario if prod["nombre"] != eliminar_nombre]

            if len(inventario) < inicial_len:
                print(f"🗑️ Producto '{eliminar_nombre}' eliminado correctamente.")
            else:
                print(f"❌ No se encontró ningún producto con el nombre '{eliminar_nombre}'.")

        elif opcion == "5":
            # FUNCIONALIDAD: Mostrar categorías únicas usando Conjuntos (Sets)
            print("\n--- Categorías Únicas de Productos ---")
            if not categorias_unicas:
                print("No hay categorías registradas aún.")
            else:
                print("Categorías registradas (sin duplicados):")
                for cat in categorias_unicas:
                    print(f"- {cat}")

        elif opcion == "6":
            print("\nGracias por utilizar el sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
