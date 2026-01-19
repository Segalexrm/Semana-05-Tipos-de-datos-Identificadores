from typing import List, Dict
from modelos.pedido import Pedido
from modelos.producto import Producto
from datetime import datetime

# Clase de servicio para manejar el restaurante
# DEMOSTRACIÓN: Gestión de múltiples objetos y encapsulación
class Restaurante:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.__pedidos: List[Pedido] = []  # Lista privada de pedidos
        self.__ventas_diarias: Dict[str, float] = {}  # Diccionario privado
        self.__contador_pedidos = 1000  # Comienza desde 1000
    
    def crear_pedido(self, cliente: str) -> Pedido:
        """Crea un nuevo pedido."""
        self.__contador_pedidos += 1
        nuevo_pedido = Pedido(self.__contador_pedidos, cliente)
        self.__pedidos.append(nuevo_pedido)
        print(f"📋 Pedido #{nuevo_pedido.numero_pedido} creado para {cliente}")
        return nuevo_pedido
    
    def procesar_pedido(self, numero_pedido: int) -> List[str]:
        """Procesa y prepara un pedido."""
        for pedido in self.__pedidos:
            if pedido.numero_pedido == numero_pedido:
                resultados = pedido.preparar_pedido()
                pedido.cambiar_estado("listo")
                self.__registrar_venta(pedido.obtener_total())
                return resultados
        return ["❌ Pedido no encontrado"]
    
    def __registrar_venta(self, monto: float) -> None:
        """Método privado para registrar ventas (encapsulación)."""
        fecha_hoy = datetime.now().strftime("%Y-%m-%d")
        if fecha_hoy in self.__ventas_diarias:
            self.__ventas_diarias[fecha_hoy] += monto
        else:
            self.__ventas_diarias[fecha_hoy] = monto
    
    def buscar_pedido_por_cliente(self, nombre_cliente: str) -> List[Pedido]:
        """Busca pedidos por nombre de cliente."""
        return [p for p in self.__pedidos if p.cliente.lower() == nombre_cliente.lower()]
    
    def obtener_pedido(self, numero_pedido: int):
        """Obtiene un pedido por su número."""
        for pedido in self.__pedidos:
            if pedido.numero_pedido == numero_pedido:
                return pedido
        return None
    
    def mostrar_estadisticas(self) -> str:
        """Muestra estadísticas del restaurante."""
        total_pedidos = len(self.__pedidos)
        pedidos_completados = len([p for p in self.__pedidos if hasattr(p, 'estado')])
        
        estadisticas = [
            f"\n📊 ESTADÍSTICAS - {self.nombre}",
            f"══════════════════════════════════════",
            f"Total pedidos creados: {total_pedidos}",
            f"Último número de pedido: {self.__contador_pedidos}",
            f"Ventas registradas: {len(self.__ventas_diarias)} días"
        ]
        
        if self.__ventas_diarias:
            hoy = datetime.now().strftime("%Y-%m-%d")
            venta_hoy = self.__ventas_diarias.get(hoy, 0)
            estadisticas.append(f"Ventas hoy: ${venta_hoy:.2f}")
        
        estadisticas.append(f"══════════════════════════════════════")
        return "\n".join(estadisticas)
    
    def listar_pedidos_activos(self) -> List[Pedido]:
        """Lista pedidos no entregados."""
        return [p for p in self.__pedidos if hasattr(p, 'estado') and p.estado != "entregado"]