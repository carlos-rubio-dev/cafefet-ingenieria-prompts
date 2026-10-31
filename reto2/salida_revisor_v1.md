\### 1. ERRORES ENCONTRADOS



\*   \*\*Error de lógica en la validación del saldo:\*\* La condición `if est.saldo - sum(p.precio 

for p in productos) < -1000:` es incorrecta. Esta expresión verifica si el saldo restante es 

menor que -1000, lo cual no tiene sentido lógico para validar que el saldo no sea negativo. 

Debería verificar si el saldo resultante es menor o igual a 0 (`<= 0`).

\*   \*\*Error de lógica en la validación del límite de productos:\*\* El código verifica `if 

len(productos) > 6`, pero la regla establece un máximo de \*\*5\*\* productos. El umbral correcto 

debería ser `> 5`.

\*   \*\*Falta de validación de días permitidos:\*\* El código no verifica si el día actual es 

válido (lunes a sábado). Solo valida la hora, ignorando los fines de semana.

\*   \*\*Falta de validación de disponibilidad de productos:\*\* El código asume que todos los 

productos en la lista `productos` están disponibles, sin verificar si alguno está agotado.

\*   \*\*Ausencia de lógica de cancelación y devolución:\*\* El código no implementa ninguna lógica 

para manejar el escenario donde un pedido se recoge después de 30 minutos (cancelación y 

devolución de saldo).



\### 2. REGLAS INCUMPLIDAS



\*   \*\*Límite de productos:\*\* Se permite pedir hasta 6 productos en lugar del máximo permitido 

de 5.

\*   \*\*Horarios de operación:\*\* No se valida que el pedido se realice exclusivamente entre lunes 

y sábado (se permite pedir los domingos y lunes si la hora coincide, o cualquier día fuera de 

semana).

\*   \*\*Validación de saldo:\*\* La lógica actual no previene transacciones que dejarían al 

estudiante con un saldo negativo; además, la condición usada es incorrecta.

\*   \*\*Disponibilidad de productos:\*\* No se evita pedir productos que ya están agotados.

\*   \*\*Manejo de cancelaciones:\*\* No existe ninguna implementación para el caso de cancelación por no recoger el pedido en 30 minutos 

ni la devolución del saldo correspondiente.



\### 3. CORRECCIONES RECOMENDADAS



\*   \*\*Corregir el límite de productos:\*\* Cambiar `if len(productos) > 6` a `if len(productos) > 5`.

\*   \*\*Corregir la validación del saldo:\*\* Cambiar la condición a `if est.saldo - sum(p.precio for p in productos) < 0:`. Esto asegura 

que el saldo restante sea estrictamente positivo (o cero, dependiendo de si se permite pagar exactamente con el saldo exacto, pero 

generalmente se requiere saldo > 0 tras la transacción).

\*   \*\*Agregar validación de días:\*\* Añadir una verificación como `if not (lunes <= dia\_actual <= sabado): return False`.

\*   \*\*Validar disponibilidad:\*\* Iterar sobre los productos y verificar su estado; si alguno está agotado, devolver `False`.

\*   \*\*Implementar lógica de cancelación:\*\* Crear una función o bloque condicional que detecte el paso de 30 minutos desde la hora del 

pedido y ejecute la devolución del saldo al carné antes de marcar el pedido como cancelado.



\### 4. RESULTADO



El código \*\*NO cumple\*\* con las reglas de CafeFET.



La justificación es contundente: el código actual permite pedidos excesivos (hasta 6 productos), permite transacciones que podrían 

dejar un saldo negativo debido a una fórmula matemática errónea, no restringe los pedidos a la semana laboral (lunes-sábado) y carece 

completamente de mecanismos para gestionar la disponibilidad de productos o las cancelaciones por tiempo de espera.

