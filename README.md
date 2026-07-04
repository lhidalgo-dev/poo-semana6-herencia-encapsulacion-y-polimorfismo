# Taller Práctico – Organización modular de un sistema orientado a objetos en Python

- **Estudiante:** Leython Josue Hidalgo Valdez
- **Asignatura:** Programación Orientada a Objetos
- **Actividad:** Semana 6 – Organización modular de un sistema orientado a objetos en Python

## Descripción del sistema

Este proyecto implementa una versión mejorada del sistema `restaurante_app`, aplicando los
principios fundamentales de la Programación Orientada a Objetos: **herencia**,
**encapsulación** y **polimorfismo**. El sistema representa productos disponibles en un
restaurante mediante una clase padre `Producto` y dos clases hijas especializadas,
`Platillo` y `Bebida`. Un servicio `Restaurante` administra la lista de productos
registrados y permite mostrar el menú completo en consola.

El programa crea dos platillos y dos bebidas, los registra en el restaurante y muestra
su información utilizando el mismo método (`mostrar_informacion()`), evidenciando cómo
cada tipo de objeto responde de forma distinta a la misma llamada.

## Estructura del proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py      # Clase padre Producto
│   ├── platillo.py       # Clase hija Platillo
│   └── bebida.py         # Clase hija Bebida
├── servicios/
│   ├── __init__.py
│   └── restaurante.py    # Clase de servicio Restaurante
└── main.py                # Punto de arranque del programa
```

- **`modelos/producto.py`**: define la clase `Producto`, con los atributos comunes a
  cualquier producto del restaurante: `nombre`, `__precio` (encapsulado) y `disponible`.
- **`modelos/platillo.py`**: define la clase `Platillo`, que hereda de `Producto` y agrega
  los atributos propios `tipo_platillo` y `tiempo_preparacion_minutos`.
- **`modelos/bebida.py`**: define la clase `Bebida`, que hereda de `Producto` y agrega los
  atributos propios `volumen_ml` y `es_alcoholica`.
- **`servicios/restaurante.py`**: define la clase `Restaurante`, encargada de almacenar los
  productos en una lista y mostrar el menú completo.
- **`main.py`**: crea los objetos, los registra en el restaurante y muestra los resultados
  en consola.

## Relación de herencia aplicada

Se aplicó una relación de herencia simple entre una clase general y dos clases
especializadas:

```
Producto
├── Platillo
└── Bebida
```

`Platillo` y `Bebida` heredan de `Producto` los atributos `nombre`, `__precio` y
`disponible`, reutilizándolos mediante `super().__init__()` en sus respectivos
constructores, y cada una agrega únicamente los atributos que le son propios (razonando
qué información pertenece a la clase padre y cuál es exclusiva de cada clase hija).

## Atributo encapsulado

El atributo `__precio` de la clase `Producto` está encapsulado (nombre con doble guion
bajo). No se accede ni se modifica directamente desde fuera de la clase; en su lugar se
utilizan los métodos:

- `obtener_precio()`: devuelve el valor actual del precio.
- `cambiar_precio(nuevo_precio)`: valida que el nuevo precio sea mayor a cero antes de
  asignarlo; si no lo es, rechaza el cambio y muestra un mensaje de error.

## Método utilizado para demostrar polimorfismo

El método `mostrar_informacion()`, definido inicialmente en `Producto`, es sobrescrito en
`Platillo` y en `Bebida` para mostrar información específica de cada tipo de producto. En
`servicios/restaurante.py`, el método `mostrar_menu()` recorre la lista de productos
registrados y llama a `producto.mostrar_informacion()` sobre cada uno; aunque la llamada es
la misma para todos los objetos, cada uno ejecuta su propia versión del método según su
clase real (Platillo o Bebida), lo que evidencia el polimorfismo.

## Reflexión

Aplicar los principios de la POO en un proyecto modular permite construir sistemas más
organizados, fáciles de mantener y de extender. La herencia evita la duplicación de código
al reutilizar los atributos y comportamientos comunes de `Producto` en `Platillo` y
`Bebida`; la encapsulación protege datos sensibles como el precio, evitando modificaciones
inválidas o accidentales; y el polimorfismo permite tratar de manera uniforme objetos de
distintas clases, simplificando el código que los administra (como en `Restaurante`).
Organizar el proyecto en módulos y paquetes (`modelos`, `servicios`) además facilita
localizar responsabilidades específicas y escalar el sistema en el futuro sin afectar el
resto del código.

## Ejecución del programa

Desde la carpeta raíz del proyecto:

```bash
cd restaurante_app
python3 main.py
```
