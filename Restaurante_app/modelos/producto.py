from abc import ABC, abstractmethod
from datetime import datetime

# Clase base abstracta para productos del restaurante
# DEMOSTRACIÓN: Abstracción y Encapsulación
class Producto(ABC):
    def __init__(self, nombre: str, precio: float, categoria: str):
        # Atributos públicos
        self.nombre = nombre
        self.categoria = categoria
        
        # Atributo privado para precio (encapsulación)
        self.__precio = precio if precio > 0 else 0.0
        
        # Atributo privado para control interno
        self.__fecha_creacion = datetime.now()
    
    # Getter para precio
    def obtener_precio(self) -> float:
        """Obtiene el precio del producto (encapsulación)."""
        return self.__precio
    
    # Setter para precio con validación
    def establecer_precio(self, nuevo_precio: float) -> bool:
        """Establece nuevo precio con validación."""
        if nuevo_precio >= 0:
            self.__precio = nuevo_precio
            return True
        return False
    
    @abstractmethod
    def preparar(self) -> str:
        """Método abstracto que cada producto implementa diferente (polimorfismo)."""
        pass
    
    @abstractmethod
    def calcular_tiempo_preparacion(self) -> int:
        """Calcula tiempo de preparación en minutos."""
        pass
    
    def obtener_info(self) -> str:
        """Información básica del producto."""
        return f"{self.nombre} (${self.obtener_precio():.2f}) - {self.categoria}"
    
    def aplicar_descuento(self, porcentaje: float) -> float:
        """Aplica descuento y retorna nuevo precio."""
        if 0 <= porcentaje <= 100:
            descuento = self.__precio * (porcentaje / 100)
            self.__precio -= descuento
            return self.__precio
        return self.__precio