Comparación de resultados — Reto 1: CafeFET



1\. Prompt malo



El modelo generó una función en JavaScript e inventó elementos que no se habían solicitado, como impuestos del 16 %, identificadores y validaciones de clientes.



Decisiones que tuvo que adivinar



1\. El lenguaje de programación.

2\. El nombre de la función.

3\. Los parámetros que debía recibir.

4\. La estructura de los datos.

5\. Las reglas de validación.

6\. El cálculo de impuestos y el resultado que debía devolver.



2\. Prompt mejorado



Al incluir los cinco bloques y las reglas dentro de las etiquetas `<reglas>`, el modelo generó una función en Python que valida los días, horarios, máximo de cinco productos, disponibilidad y saldo del estudiante.



Sin embargo, no implementó la cancelación ni la devolución del saldo después de 30 minutos. Además, no permite pedidos exactamente a las 18:00.



3\. Prompt variante



Se modificó únicamente el bloque de restricciones. El modelo generó una función que siempre devuelve `True`, sin validar horarios, cantidad de productos, saldo ni disponibilidad.



4\. Conclusión



El ejercicio demostró que un prompt claro y detallado permite obtener respuestas más cercanas a lo que necesita el negocio. El prompt mejorado logró que el modelo aplicara varias reglas de CafeFET, mientras que la variante mostró cómo cambia el resultado al modificar las restricciones. También se evidenció que es necesario revisar las respuestas, porque el modelo puede dejar reglas sin implementar.

