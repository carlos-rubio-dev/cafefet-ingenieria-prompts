Criterio 1:

Dado que soy un estudiante registrado en el sistema CafeFET,

Cuando accedo a la sección de "Últimos Pedidos" y selecciono una opción para repetir mi pedido más reciente,

Entonces el sistema debe mostrar exactamente los mismos productos del pedido anterior sin permitir añadir ni eliminar artículos.



Criterio 2:

Dado que estoy intentando agregar un producto al pedido repetido,

Cuando intento seleccionar más de 5 productos en total (incluyendo los del pedido original),

Entonces el sistema debe bloquear la acción y mostrar un mensaje de error indicando que se ha alcanzado el límite máximo de 5 

productos por pedido.



Criterio 3:

Dado que estoy intentando añadir un producto al pedido repetido,

Cuando selecciono un artículo que aparece como "Agotado" en el catálogo actual,

Entonces el sistema debe impedir la selección y mostrar un mensaje indicando que el producto no está disponible para pedidos.



Criterio 4:

Dado que mi saldo del carné es suficiente para cubrir el valor total de los productos repetidos,

Cuando procedo al pago finalizando la compra,

Entonces el sistema debe restar el monto correspondiente a mi saldo y confirmar exitosamente la realización del pedido sin dejar un 

saldo negativo.



