| Caso | Entrada | Resultado esperado | Criterio que cubre |

| :--- | :--- | :--- | :--- |

| 1 | Estudiante accede a la función "Repetir pedido" tras haber realizado un pedido válido (ej. 3 productos: Café, Leche, Pan) 

dentro del horario de atención (Lunes-Sábado, 07:00-18:00). El sistema muestra los mismos productos y cantidades sin permitir 

cambios. | Se visualiza el formulario con los productos y cantidades exactos del pedido anterior. No aparecen campos para modificar 

cantidades ni eliminar ítems. El botón "Finalizar compra" es funcional. | Criterio 1 |

| 2 | Estudiante intenta repetir un pedido que contiene exactamente 6 productos (ej. Café, Leche, Pan, Galleta, Helado, Postre). Al 

hacer clic en "Repetir pedido". | Aparece un mensaje de error: "Se ha excedido el límite máximo de 5 productos". El botón "Finalizar 

compra" no se activa ni permite la transacción. | Criterio 2 |

| 3 | Estudiante intenta repetir un pedido que incluye un producto actualmente agotado (ej. Café, Leche, Pan, Helado-Agotado). Al 

hacer clic en "Repetir pedido". | Aparece un mensaje de error: "Los productos seleccionados no están disponibles". El botón 

"Finalizar compra" no se activa ni permite la transacción. | Criterio 3 |

| 4 | Estudiante intenta repetir un pedido cuyo saldo total es de $15.00, pero su saldo actual en el carné es de $10.00. Al hacer 

clic en "Repetir pedido". | Aparece un mensaje de error: "No hay suficiente saldo". El botón "Finalizar compra" no se activa ni 

permite la transacción. | Criterio 4 |



\### Auto-verificación



\*   \*\*Criterio 1:\*\* Cubierto por el Caso 1 (Escenario positivo de repetición exitosa).

\*   \*\*Criterio 2:\*\* Cubierto por el Caso 2 (Escenario negativo por límite de productos).

\*   \*\*Criterio 3:\*\* Cubierto por el Caso 3 (Escenario negativo por stock agotado).

\*   \*\*Criterio 4:\*\* Cubierto por el Caso 4 (Escenario negativo por saldo insuficiente).



\*\*Nota sobre restricciones:\*\* Se ha respetado estrictamente la información proporcionada. No se han inventado comportamientos 

adicionales como la posibilidad de modificar el pedido repetido (se asume que no se permite según el criterio 1) ni mensajes 

específicos más allá de lo descrito en los criterios ("mostrar un mensaje indicando...").



