La función `crear\_pedido` está diseñada para crear un pedido en una tienda de café, con la condición de que el estudiante no pueda 

pedir más de 6 productos. Sin embargo, hay un problema con la lógica de la función que permite pasar un pedido inválido, incluso 

cuando el estudiante tiene saldo suficiente y la hora es 10:00.



Aquí está el desglose de la función:



1\. La función verifica si el número de productos en el pedido (`len(productos)`) es mayor de 6. Si lo es, devuelve `False`, lo que 

significa que el pedido es inválido.



2\. La función luego calcula la cantidad total de dinero que se necesitaría para los productos en el pedido (`sum(p.precio for p in 

productos)`) y verifica si el saldo del estudiante (`est.saldo`) menos esta cantidad total es menor que -1000. Si lo es, devuelve 

`False`, lo que significa que el pedido es inválido.



3\. La función final verifica si la hora es entre las 7:00 y las 18:00 (inclusive). Si lo es, devuelve `True`, lo que significa que el 

pedido es válido.



Sin embargo, hay un problema con la lógica de la función. La condición `if est.saldo - sum(p.precio for p in productos) < -1000:` 

verifica si el saldo del estudiante es menos que -1000 después de pagar por los productos. Sin embargo, esto no verifica si el saldo 

del estudiante es suficiente para cubrir el costo de los productos. En su lugar, debería verificar si el saldo del estudiante es 

mayor o igual al costo total de los productos (`est.saldo >= sum(p.precio for p in productos)`).



Además, la condición `if len(productos) > 6:` solo verifica si hay más de 6 productos en el pedido. Sin embargo, no verifica si el 

número de productos es exactamente 6. En su lugar, debería verificar si el número de productos es menor o igual a 6 (`len(productos) 

<= 6`).



Por lo tanto, la función permite pasar un pedido inválido porque no verifica correctamente si el saldo del estudiante es suficiente 

para cubrir el costo de los productos y si el número de productos es exactamente 6. Para corregir estos problemas, la función debería 

ser modificada para incluir las condiciones corregidas mencionadas anteriormente.

