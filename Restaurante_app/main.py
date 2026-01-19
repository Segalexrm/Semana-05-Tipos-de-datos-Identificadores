from modelos.hamburguesa import Hamburguesa
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

def main():
    """
    RESTAURANTE
    ===========
    """
    
    print("=" * 20)
    print("SISTEMA DE RESTAURANTE")
    print("=" * 20)
    
    # Crear restaurante
    print("\n🏪 INICIANDO RESTAURANTE...")
    restaurante = Restaurante("Restaurante")
    
    # Crear productos disponibles
    print("\n📦 CREANDO PRODUCTOS DISPONIBLES:")
    
    # Hamburguesas
    hamburguesa_clasica = Hamburguesa(
        "Clásica", 
        8.50, 
        ["pan", "carne", "lechuga", "tomate", "queso"], 
        "normal"
    )
    
    hamburguesa_especial = Hamburguesa(
        "Especial BBQ", 
        12.75, 
        ["pan brioche", "doble carne", "cebolla crispy", 
         "tocino", "queso cheddar", "salsa BBQ"], 
        "doble"
    )
    
    # Bebidas
    refresco_cola = Bebida("Refresco Cola", 2.50, 500, True)
    jugo_naranja = Bebida("Jugo de Naranja", 3.25, 400, False)
    agua_mineral = Bebida("Agua Mineral", 1.75, 600, True)
    
    # Mostrar productos
    productos = [hamburguesa_clasica, hamburguesa_especial, 
                 refresco_cola, jugo_naranja, agua_mineral]
    
    for producto in productos:
        print(f"  ✅ {producto.obtener_info()}")
    
    # Procesar pedidos
    print("\n" + "=" * 20)
    print("📝 PROCESANDO PEDIDOS DE CLIENTES")
    print("=" * 20)
    
    # Pedido 1
    print("\n👤 CLIENTE: Alejandro Moreno")
    pedido1 = restaurante.crear_pedido("Alejandro Moreno")
    pedido1.agregar_producto(hamburguesa_clasica)
    pedido1.agregar_producto(refresco_cola)
    
    # Demostrar método específico de Hamburguesa
    print(f"\n🔧 Personalizando pedido:")
    print(hamburguesa_clasica.agregar_ingrediente_extra("pepinillos", 0.50))
    
    # Pedido 2
    print("\n👤 CLIENTE: María Gómez")
    pedido2 = restaurante.crear_pedido("María Gómez")
    pedido2.agregar_producto(hamburguesa_especial)
    pedido2.agregar_producto(jugo_naranja)
    pedido2.agregar_producto(agua_mineral)
    
    # Demostrar método específico de Bebida
    print(f"\n🔧 Personalizando bebida:")
    print(jugo_naranja.cambiar_temperatura("fría"))
    
    # Mostrar resumen de pedidos
    print("\n" + "=" * 20)
    print("📋 RESUMEN DE PEDIDOS")
    print("=" * 20)
    
    print("\n" + pedido1.obtener_resumen())
    print("\n" + pedido2.obtener_resumen())
    
    # Procesar pedidos (demostrar polimorfismo)
    print("\n" + "=" * 20)
    print("👨‍🍳 PREPARANDO PEDIDOS")
    print("=" * 20)
    
    for pedido in [pedido1, pedido2]:
        resultado = restaurante.procesar_pedido(pedido.numero_pedido)
        for linea in resultado:
            print(linea)
        print("-" * 20)
    
    # Demostrar búsqueda
    print("\n" + "=" * 20)
    print("🔍 BUSCANDO PEDIDOS DE 'Alejandro Moreno'")
    print("=" * 20)
    
    pedidos_alejandro = restaurante.buscar_pedido_por_cliente("Alejandro Moreno")
    for pedido in pedidos_alejandro:
        print(f"\nPedido encontrado: #{pedido.numero_pedido}")
        print(f"Total: ${pedido.obtener_total():.2f}")
    
    
    # Intentar acceder directamente al precio (no permitido)
    print("Acceso controlado al precio:")
    print(f"  - Vía getter: ${hamburguesa_clasica.obtener_precio():.2f}")
    # print(hamburguesa_clasica.__precio)  # Esto generaría AttributeError
    
    # Aplicar descuento (usando método público)
    print(f"\nAplicando 10% de descuento a {hamburguesa_especial.nombre}:")
    nuevo_precio = hamburguesa_especial.aplicar_descuento(10)
    print(f"  Nuevo precio: ${nuevo_precio:.2f}")
    
    # Estadísticas del restaurante
    print("\n" + "=" * 20)
    print("📊 REPORTE FINAL DEL SISTEMA")
    print("=" * 20)
    
    print(restaurante.mostrar_estadisticas())
    
   
    print("\n" + "=" * 20)
    print("✅ SISTEMA EJECUTADO CORRECTAMENTE")
    print("=" * 20)

if __name__ == "__main__":
    main()