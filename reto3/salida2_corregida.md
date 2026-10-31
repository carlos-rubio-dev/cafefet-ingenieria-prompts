Criterio 1:

Dado que el estudiante ha realizado un pedido válido en una fecha y hora dentro del horario de atención (lunes a sábado, 7:00 a 

18:00),

Cuando accede al sistema para repetir su último pedido con un solo clic,

Entonces el sistema debe mostrar exactamente los mismos productos y cantidades que se encontraban en su pedido anterior sin permitir 

modificaciones.



Criterio 2:

Dado que el estudiante intenta repetir un pedido que contiene más de 5 productos,

Cuando ejecuta la acción de "Repetir pedido" con un solo clic,

Entonces el sistema debe mostrar un mensaje de error indicando que se ha excedido el límite máximo de 5 productos y no debe permitir 

finalizar la compra.



Criterio 3:

Dado que el estudiante intenta repetir un pedido que incluye productos actualmente agotados en el inventario,

Cuando ejecuta la acción de "Repetir pedido" con un solo clic,

Entonces el sistema debe mostrar un mensaje indicando que los productos seleccionados no están disponibles y no debe permitir 

finalizar la compra.



Criterio 4:

Dado que el estudiante intenta repetir un pedido cuyo saldo total supera su saldo actual en el carné,

Cuando ejecuta la acción de "Repetir pedido" con un solo clic,

Entonces el sistema debe mostrar un mensaje indicando que no hay suficiente saldo y no debe permitir finalizar la compra.

