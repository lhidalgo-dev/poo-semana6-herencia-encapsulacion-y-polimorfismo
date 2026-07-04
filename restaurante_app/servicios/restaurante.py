"""
Módulo que define la clase de servicio Restaurante.

Se encarga de administrar la lista de productos registrados
(platillos y bebidas) y de mostrar la información del menú.
"""


class Restaurante:
    """
    Clase de servicio encargada de administrar los productos
    disponibles en el restaurante.

    Atributos:
        nombre_restaurante (str): Nombre comercial del restaurante.
        productos_registrados (list): Lista de objetos Producto
            (instancias de Platillo o Bebida) registrados.
    """

    def __init__(self, nombre_restaurante):
        """
        Inicializa el restaurante con un nombre y una lista vacía
        de productos registrados.

        Args:
            nombre_restaurante (str): Nombre comercial del restaurante.
        """
        self.nombre_restaurante = nombre_restaurante
        self.productos_registrados = []

    def agregar_producto(self, producto):
        """
        Agrega un producto (Platillo o Bebida) a la lista del restaurante.

        Args:
            producto (Producto): Instancia de Platillo o Bebida a registrar.
        """
        self.productos_registrados.append(producto)
        print(f"Se registró '{producto.nombre}' en el menú de {self.nombre_restaurante}.")

    def mostrar_menu(self):
        """
        Recorre la lista de productos registrados y muestra su
        información en consola.

        Aquí se evidencia el polimorfismo: cada objeto ejecuta su
        propia versión de mostrar_informacion() según su tipo
        (Platillo o Bebida), aunque se invoque el mismo método.
        """
        print(f"\n===== Menú de {self.nombre_restaurante} =====")

        if not self.productos_registrados:
            print("Aún no hay productos registrados en el menú.")
            return

        for producto in self.productos_registrados:
            producto.mostrar_informacion()

        print("=" * 40)
