Para evaluar la función `crear\_pedido` con los datos proporcionados, desglosaremos cada condición `if` paso a paso:



1\. \*\*Condición 1: `if len(productos) > 6:`\*\*

&#x20;  - \*\*Qué está verificando:\*\* Número de productos en el pedido.

&#x20;  - \*\*Qué valores utiliza:\*\* El número de productos en el pedido, que es 6.

&#x20;  - \*\*Cuánto da la operación:\*\* La operación `len(productos)` devuelve 6.

&#x20;  - \*\*Si la condición es verdadera o falsa:\*\* Falsa, porque 6 no es mayor que 6.

&#x20;  - \*\*Si la función continúa o devuelve False:\*\* La función continúa, ya que la condición es falsa.



2\. \*\*Condición 2: `if est.saldo - sum(p.precio for p in productos) < -1000:`\*\*

&#x20;  - \*\*Qué está verificando:\*\* Si el saldo del estudiante después de pagar por los productos es menor que -1000.

&#x20;  - \*\*Qué valores utiliza:\*\*

&#x20;    - Saldo del estudiante: $10.000.

&#x20;    - Precios de los productos: Cada producto cuesta $1.000, y hay 6 productos, por lo que el total es $6.000.

&#x20;  - \*\*Cuánto da la operación:\*\*

&#x20;    - Saldo del estudiante: $10.000.

&#x20;    - Total de los productos: $6.000.

&#x20;    - Saldo después de pagar: $10.000 - $6.000 = $4.000.

&#x20;  - \*\*Si la condición es verdadera o falsa:\*\* Falsa, porque $4.000 no es menor que -$1.000.

&#x20;  - \*\*Si la función continúa o devuelve False:\*\* La función continúa, ya que la condición es falsa.



3\. \*\*Condición 3: `return 7 <= hora <= 18:`\*\*

&#x20;  - \*\*Qué está verificando:\*\* Si la hora del pedido está entre las 7:00 y las 18:00 (inclusive).

&#x20;  - \*\*Qué valores utiliza:\*\* La hora del pedido, que es 10:00.

&#x20;  - \*\*Cuánto da la operación:\*\* La operación `7 <= hora <= 18` se evalúa como True, porque 10:00 está entre 7:00 y 18:00.

&#x20;  - \*\*Si la condición es verdadera o falsa:\*\* Verdadera.

&#x20;  - \*\*Si la función continúa o devuelve False:\*\* La función devuelve True, porque la condición es verdadera.



\*\*Resultado Final de la Función:\*\*

La función `crear\_pedido` devuelve True, ya que todas las condiciones `if` son falsas o verdaderas, permitiendo así el pedido.



\*\*¿Debería el pedido permitirse según las reglas de CafeFET?\*\*

Basado en las reglas de CafeFET, el pedido debería permitirse, ya que el número de productos no excede el límite, el saldo del 

estudiante después de pagar es positivo, y la hora del pedido está dentro del rango permitido.

