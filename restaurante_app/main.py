"""
Punto de arranque del sistema restaurante_app.

Crea instancias de Platillo y Bebida, las registra en el servicio
Restaurante y muestra la información resultante en consola,
demostrando herencia, encapsulación y polimorfismo.
"""

from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante


def main():
    """Función principal que ejecuta el flujo del programa."""

    # Creamos el servicio principal del restaurante
    restaurante = Restaurante("Sabores del Valle")

    # Creación de objetos Platillo (clase hija de Producto)
    ceviche_camaron = Platillo(
        nombre="Ceviche de camarón",
        precio=8.50,
        tipo_platillo="Entrada",
        tiempo_preparacion_minutos=15
    )

    lomo_saltado = Platillo(
        nombre="Lomo saltado",
        precio=12.00,
        tipo_platillo="Plato fuerte",
        tiempo_preparacion_minutos=25
    )

    # Creación de objetos Bebida (clase hija de Producto)
    jugo_naranja = Bebida(
        nombre="Jugo de naranja natural",
        precio=2.50,
        volumen_ml=300,
        es_alcoholica=False
    )

    cerveza_artesanal = Bebida(
        nombre="Cerveza artesanal",
        precio=4.00,
        volumen_ml=355,
        es_alcoholica=True
    )

    # Registramos los productos en el restaurante
    restaurante.agregar_producto(ceviche_camaron)
    restaurante.agregar_producto(lomo_saltado)
    restaurante.agregar_producto(jugo_naranja)
    restaurante.agregar_producto(cerveza_artesanal)

    # Mostramos el menú completo (demostración de polimorfismo)
    restaurante.mostrar_menu()

    # Demostración de encapsulación: obtener_precio() y cambiar_precio()
    # controlan el acceso al atributo privado __precio
    print("\n--- Prueba de encapsulación sobre el precio ---")
    print(f"Precio actual de '{lomo_saltado.nombre}': ${lomo_saltado.obtener_precio():.2f}")

    lomo_saltado.cambiar_precio(13.50)
    print(f"Nuevo precio de '{lomo_saltado.nombre}': ${lomo_saltado.obtener_precio():.2f}")

    # Intento de asignar un precio inválido (debe ser rechazado)
    lomo_saltado.cambiar_precio(-5)


if __name__ == "__main__":
    main()
