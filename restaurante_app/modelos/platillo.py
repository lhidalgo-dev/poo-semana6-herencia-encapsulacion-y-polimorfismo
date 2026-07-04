"""
Módulo que define la clase Platillo, hija de Producto.

Representa una comida o plato preparado que se ofrece en el
restaurante, añadiendo atributos propios que no aplican a
un producto genérico ni a una bebida.
"""

from modelos.producto import Producto


class Platillo(Producto):
    """
    Clase hija que representa un platillo del restaurante.

    Hereda de Producto los atributos comunes (nombre, precio,
    disponibilidad) y agrega atributos específicos de un platillo:
    tipo de platillo y tiempo de preparación.
    """

    def __init__(self, nombre, precio, tipo_platillo, tiempo_preparacion_minutos, disponible=True):
        """
        Inicializa un platillo reutilizando el constructor de la
        clase padre mediante super() y añadiendo atributos propios.

        Args:
            nombre (str): Nombre del platillo.
            precio (float): Precio del platillo.
            tipo_platillo (str): Categoría del platillo (ej. entrada, fuerte, postre).
            tiempo_preparacion_minutos (int): Tiempo estimado de preparación en minutos.
            disponible (bool): Disponibilidad del platillo.
        """
        super().__init__(nombre, precio, disponible)
        self.tipo_platillo = tipo_platillo
        self.tiempo_preparacion_minutos = tiempo_preparacion_minutos

    def mostrar_informacion(self):
        """
        Sobrescribe el método de la clase padre para mostrar
        información específica de un platillo (polimorfismo).
        """
        estado = "Disponible" if self.disponible else "No disponible"
        print(
            f"Platillo: {self.nombre} | Tipo: {self.tipo_platillo} | "
            f"Precio: ${self.obtener_precio():.2f} | "
            f"Tiempo de preparación: {self.tiempo_preparacion_minutos} min | "
            f"Estado: {estado}"
        )
