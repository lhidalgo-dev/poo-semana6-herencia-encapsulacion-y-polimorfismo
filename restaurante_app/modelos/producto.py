"""
Módulo que define la clase padre Producto.

Representa un producto genérico disponible en el restaurante y
concentra los atributos y comportamientos comunes a cualquier
producto, sin importar si luego se especializa como Platillo o Bebida.
"""


class Producto:
    """
    Clase padre que representa un producto general del restaurante.

    Atributos:
        nombre (str): Nombre del producto.
        __precio (float): Precio del producto (atributo encapsulado).
        disponible (bool): Indica si el producto está disponible para la venta.
    """

    def __init__(self, nombre, precio, disponible=True):
        """
        Inicializa un producto con sus datos básicos.

        Args:
            nombre (str): Nombre del producto.
            precio (float): Precio de venta del producto.
            disponible (bool): Disponibilidad inicial del producto.
        """
        self.nombre = nombre
        self.__precio = precio  # Atributo encapsulado (privado)
        self.disponible = disponible

    def obtener_precio(self):
        """
        Devuelve el precio actual del producto.

        Este método permite el acceso controlado al atributo
        encapsulado __precio, en lugar de exponerlo directamente.

        Returns:
            float: Precio actual del producto.
        """
        return self.__precio

    def cambiar_precio(self, nuevo_precio):
        """
        Modifica el precio del producto, validando que el nuevo
        valor sea mayor a cero antes de asignarlo.

        Args:
            nuevo_precio (float): Nuevo precio propuesto para el producto.

        Returns:
            bool: True si el precio fue actualizado correctamente,
                  False si el valor no era válido.
        """
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
            return True

        print(f"Error: el precio de '{self.nombre}' no puede ser negativo ni igual a cero.")
        return False

    def mostrar_informacion(self):
        """
        Muestra la información general del producto en consola.

        Este método es sobrescrito por las clases hijas Platillo y
        Bebida para demostrar el principio de polimorfismo.
        """
        estado = "Disponible" if self.disponible else "No disponible"
        print(f"Producto: {self.nombre} | Precio: ${self.obtener_precio():.2f} | Estado: {estado}")
