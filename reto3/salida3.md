| Caso | Entrada | Resultado esperado | Criterio que cubre |

|------|---------|---------------------|---------------------|

| 1 (Positivo) | Estudiante accede a "Repetir pedido" tras haber realizado un pedido válido el día martes a las 10:00 AM con 3

productos (Café, Leche, Galleta). El sistema muestra los mismos ítems y cantidades. | Se visualizan exactamente los productos y

cantidades del pedido anterior sin opciones para modificar ni eliminar ítems. | Criterio 1 |

| 2 (Negativo) | Estudiante intenta repetir un pedido histórico que contenía 6 productos (Café x2, Leche x2, Galleta x1, Agua x1). Al

hacer clic en "Repetir pedido", el sistema muestra la lista de productos. | Aparece un mensaje de error: "Se ha excedido el límite

máximo de 5 productos". El botón de finalizar compra no está habilitado ni se puede agregar más ítems. | Criterio 2 |

| 3 (Negativo) | Estudiante intenta repetir un pedido que incluye "Helado" y "Postre", los cuales están marcados como "Agotados" en

el inventario actual. Al hacer clic en "Repetir pedido". | Aparece un mensaje de error: "Los productos seleccionados no están

disponibles". El proceso de compra se detiene sin permitir finalizar. | Criterio 3 |

| 4 (Negativo) | Estudiante tiene un saldo de $10.00 en su carné. Intenta repetir un pedido cuyo total es $15.00. Al hacer clic en

"Repetir pedido". | Aparece un mensaje de error: "No hay suficiente saldo para completar la compra". El proceso se detiene sin

permitir finalizar. | Criterio 4 |



\### Auto-verificación

\*   \*\*Criterio 1\*\*: ✅ Cubierto por el Caso 1 (Positivo). Verifica que el sistema repita ítems y cantidades exactas sin permitir

cambios.

\*   \*\*Criterio 2\*\*: ✅ Cubierto por el Caso 2 (Negativo). Verifica el límite de 5 productos.

\*   \*\*Criterio 3\*\*: ✅ Cubierto por el Caso 3 (Negativo). Verifica la disponibilidad de productos agotados.

\*   \*\*Criterio 4\*\*: ✅ Cubierto por el Caso 4 (Negativo). Verifica la verificación de saldo del carné.



Todos los criterios de aceptación han sido convertidos en casos de prueba verificables con datos concretos. No se han inventado

reglas adicionales; solo se ha aplicado la lógica descrita en los criterios.

