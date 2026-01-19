from modelos.producto import Producto

# DEMOSTRACIÓN: Herencia y Polimorfismo
class Hamburguesa(Producto):
    def __init__(self, nombre: str, precio: float, ingredientes: list, tamaño: str = "normal"):
        super().__init__(nombre, precio, "Hamburguesa")
        
        # Atributos específicos de Hamburguesa
        self.ingredientes = ingredientes
        self.tamaño = tamaño
        self.__estado = "sin preparar"  # Atributo privado
    
    # Implementación del método abstracto (polimorfismo)
    def preparar(self) -> str:
        """Preparación específica para hamburguesas."""
        pasos = [
            f"1. Calentando pan para {self.nombre}",
            f"2. Cocinando carne ({self.tamaño})",
            f"3. Agregando ingredientes: {', '.join(self.ingredientes)}",
            f"4. Ensamblando hamburguesa",
            f"5. Empaquetando"
        ]
        
        self.__estado = "preparada"
        return "\n".join(pasos)
    
    # Implementación del método abstracto (polimorfismo)
    def calcular_tiempo_preparacion(self) -> int:
        """Tiempo de preparación basado en tamaño e ingredientes."""
        tiempo_base = 5
        if self.tamaño == "grande":
            tiempo_base += 3
        elif self.tamaño == "doble":
            tiempo_base += 5
        
        tiempo_extra = len(self.ingredientes) * 0.5
        return int(tiempo_base + tiempo_extra)
    
    # Método específico de Hamburguesa
    def agregar_ingrediente_extra(self, ingrediente: str, costo_extra: float = 1.0) -> str:
        """Agrega ingrediente extra a la hamburguesa."""
        self.ingredientes.append(ingrediente)
        nuevo_precio = self.obtener_precio() + costo_extra
        self.establecer_precio(nuevo_precio)
        return f"✅ {ingrediente} agregado. Nuevo precio: ${nuevo_precio:.2f}"
    
    def obtener_detalles(self) -> str:
        """Detalles específicos de la hamburguesa."""
        return f"{super().obtener_info()}\nTamaño: {self.tamaño}\nIngredientes: {', '.join(self.ingredientes)}"