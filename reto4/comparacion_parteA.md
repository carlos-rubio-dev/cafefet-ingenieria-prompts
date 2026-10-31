Reto 4 – Parte A: Comparación de resultados



Primera prueba: pregunta breve



Se preguntó por qué la función `crear\_pedido` permite pasar un pedido inválido.



El modelo identificó parcialmente el error del límite de productos y detectó el problema de la validación del saldo. Sin embargo, propuso una corrección incorrecta para el límite, porque mantuvo el valor de 6 en lugar de aplicar el máximo de 5 productos establecido por CafeFET. Tampoco identificó la falta de validación de los días permitidos ni la cancelación y devolución del saldo después de 30 minutos.



Errores identificados: 2, aunque uno fue corregido incorrectamente.



Segunda prueba: evaluación paso a paso



Se utilizaron datos concretos: saldo de $10.000, seis productos de $1.000 cada uno y hora de las 10:00.



El modelo evaluó cada condición y calculó correctamente que el saldo restante sería de $4.000 y que la hora estaba dentro del horario permitido. Sin embargo, no identificó que seis productos superan el máximo permitido de cinco.



Errores identificados: 0 errores de la función detectados correctamente con este caso concreto.



Comparación y conclusión



La primera pregunta permitió que el modelo identificara más problemas de la función, aunque no propuso correctamente todas las correcciones. La segunda pregunta produjo una explicación más detallada de las condiciones y sus valores, pero no logró detectar el error del límite de productos.



Esto demuestra que pedir una evaluación paso a paso ayuda a observar cómo se ejecuta cada condición, pero no garantiza que el modelo interprete correctamente las reglas del negocio. Es necesario proporcionarle datos adecuados y comprobar sus conclusiones.

