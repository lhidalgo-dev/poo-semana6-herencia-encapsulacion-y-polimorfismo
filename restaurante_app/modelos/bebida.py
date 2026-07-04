"""
Módulo que define la clase Bebida, hija de Producto.

Representa una bebida disponible en el restaurante, añadiendo
atributos propios que no aplican a un producto genérico ni a
un platillo.
"""

from modelos.producto import Producto


class Bebida(Producto):
    """
    Clase hija que representa una bebida del restaurante.

    Hereda de Producto los atributos comunes (nombre, precio,
    disponibilidad) y agrega atributos específicos de una bebida:
    volumen en mililitros y si contiene alcohol.
    """

    def __init__(self, nombre, precio, volumen_ml, es_alcoholica=False, disponible=True):
        """
        Inicializa una bebida reutilizando el constructor de la
        clase padre mediante super() y añadiendo atributos propios.

        Args:
            nombre (str): Nombre de la bebida.
            precio (float): Precio de la bebida.
            volumen_ml (int): Volumen de la bebida en mililitros.
            es_alcoholica (bool): Indica si la bebida contiene alcohol.
            disponible (bool): Disponibilidad de la bebida.
        """
        super().__init__(nombre, precio, disponible)
        self.volumen_ml = volumen_ml
        self.es_alcoholica = es_alcoholica

    def mostrar_informacion(self):
        """
        Sobrescribe el método de la clase padre para mostrar
        información específica de una bebida (polimorfismo).
        """
        estado = "Disponible" if self.disponible else "No disponible"
        tipo_alcohol = "Alcohólica" if self.es_alcoholica else "No alcohólica"
        print(
            f"Bebida: {self.nombre} | Volumen: {self.volumen_ml} ml | "
            f"Precio: ${self.obtener_precio():.2f} | "
            f"Tipo: {tipo_alcohol} | Estado: {estado}"
        )
