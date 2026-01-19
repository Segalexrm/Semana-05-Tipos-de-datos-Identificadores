from modelos.producto import Producto

# DEMOSTRACIÓN: Herencia y Polimorfismo
class Bebida(Producto):
    def __init__(self, nombre: str, precio: float, tamaño_ml: int, con_hielo: bool = True):
        super().__init__(nombre, precio, "Bebida")
        
        # Atributos específicos de Bebida
        self.tamaño_ml = tamaño_ml
        self.con_hielo = con_hielo
        self.__temperatura = "ambiente"  # Atributo privado
    
    # Implementación diferente del método abstracto (polimorfismo)
    def preparar(self) -> str:
        """Preparación específica para bebidas."""
        preparacion = [f"1. Tomando {self.nombre} de {self.tamaño_ml}ml"]
        
        if self.con_hielo:
            preparacion.append("2. Agregando hielo")
            self.__temperatura = "fría"
        else:
            preparacion.append("2. Sin hielo")
        
        if "refresco" in self.nombre.lower():
            preparacion.append("3. Llenando con gas carbónico")
        elif "jugo" in self.nombre.lower():
            preparacion.append("3. Mezclando concentrado")
        
        preparacion.append("4. Colocando pajilla/tapa")
        return "\n".join(preparacion)
    
    # Implementación diferente del método abstracto (polimorfismo)
    def calcular_tiempo_preparacion(self) -> int:
        """Tiempo de preparación para bebidas."""
        tiempo = 1  # minuto base
        
        if self.tamaño_ml > 500:
            tiempo += 1
        if not self.con_hielo:
            tiempo += 1  # Tiempo extra para enfriar sin hielo
        
        return tiempo
    
    # Método específico de Bebida
    def cambiar_temperatura(self, temp: str) -> str:
        """Cambia la temperatura de la bebida."""
        temperaturas_validas = ["fría", "tibia", "caliente", "ambiente"]
        if temp in temperaturas_validas:
            self.__temperatura = temp
            return f"Temperatura cambiada a {temp}"
        return "Temperatura no válida"
    
    def obtener_detalles(self) -> str:
        """Detalles específicos de la bebida."""
        hielo = "con hielo" if self.con_hielo else "sin hielo"
        return f"{super().obtener_info()}\nTamaño: {self.tamaño_ml}ml\n{hielo}"