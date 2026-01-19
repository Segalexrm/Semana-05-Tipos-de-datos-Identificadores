from typing import List
from datetime import datetime
from modelos.producto import Producto

# Clase para manejar pedidos
# DEMOSTRACIÓN: Composición y Encapsulación
class Pedido:
    def __init__(self, numero_pedido: int, cliente: str):
        # Atributos públicos
        self.numero_pedido = numero_pedido
        self.cliente = cliente
        
        # Atributos privados (encapsulación)
        self.__productos: List[Producto] = []
        self.__fecha_hora = datetime.now()
        self.__estado = "pendiente"
        self.__total = 0.0
    
    def agregar_producto(self, producto: Producto) -> str:
        """Agrega un producto al pedido."""
        self.__productos.append(producto)
        self.__calcular_total()
        return f"✅ {producto.nombre} agregado al pedido #{self.numero_pedido}"
    
    def eliminar_producto(self, nombre_producto: str) -> bool:
        """Elimina un producto del pedido."""
        for i, producto in enumerate(self.__productos):
            if producto.nombre == nombre_producto:
                self.__productos.pop(i)
                self.__calcular_total()
                return True
        return False
    
    def __calcular_total(self) -> None:
        """Método privado para calcular total (encapsulación)."""
        self.__total = sum(p.obtener_precio() for p in self.__productos)
    
    def obtener_total(self) -> float:
        """Getter para el total."""
        return self.__total
    
    def cambiar_estado(self, nuevo_estado: str) -> str:
        """Cambia el estado del pedido."""
        estados_validos = ["pendiente", "en preparación", "listo", "entregado", "cancelado"]
        if nuevo_estado in estados_validos:
            self.__estado = nuevo_estado
            return f"Estado cambiado a: {nuevo_estado}"
        return "Estado no válido"
    
    def preparar_pedido(self) -> List[str]:
        """Prepara todos los productos del pedido (polimorfismo)."""
        resultados = []
        resultados.append(f"\n🍽️ Preparando pedido #{self.numero_pedido} para {self.cliente}")
        
        for producto in self.__productos:
            resultados.append(f"\n🔹 {producto.nombre}:")
            resultados.append(producto.preparar())
            resultados.append(f"   ⏰ Tiempo estimado: {producto.calcular_tiempo_preparacion()} min")
        
        self.__estado = "en preparación"
        return resultados
    
    def obtener_resumen(self) -> str:
        """Resumen del pedido."""
        resumen = [
            f"══════════",
            f"PEDIDO #{self.numero_pedido}",
            f"══════════",
            f"Cliente: {self.cliente}",
            f"Fecha: {self.__fecha_hora.strftime('%d/%m/%Y %H:%M')}",
            f"Estado: {self.__estado}",
            f"══════════",
            f"PRODUCTOS:"
        ]
        
        for i, producto in enumerate(self.__productos, 1):
            resumen.append(f"{i}. {producto.obtener_info()}")
        
        resumen.append(f"═══════")
        resumen.append(f"TOTAL: ${self.__total:.2f}")
        resumen.append(f"═══════")
        
        return "\n".join(resumen)