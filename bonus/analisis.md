Análisis de resultados – Reto 5 Bonus

Proyecto CafeFET



1\. Comparación de las versiones de los prompts

Se realizaron pruebas con dos versiones de prompts y dos modelos de lenguaje: qwen3.5:4b y qwen3.5:0.8b. La versión V1 utiliza instrucciones sencillas, mientras que la versión V2 incorpora definiciones de las categorías y ejemplos para orientar la clasificación.

Con el modelo qwen3.5:4b, la versión V1 obtuvo 7 aciertos de 10, equivalentes al 70 %. Al utilizar la versión V2, obtuvo 10 aciertos de 10, alcanzando el 100 %.

Por otro lado, el modelo qwen3.5:0.8b obtuvo 7 aciertos de 10 con la versión V1, es decir, un 70 %. Con la versión V2 consiguió 9 aciertos de 10, equivalentes al 90 %.

Estos resultados muestran que la versión V2 obtuvo un mejor desempeño con ambos modelos. Esto indica que proporcionar definiciones y ejemplos ayuda a mejorar la interpretación de los mensajes.



2\. ¿Qué sucede cuando falta un dato?

En la generación de reportes JSON, los modelos pueden utilizar valores null cuando no se proporciona información, como la hora de recogida o la cantidad de un producto.

Sin embargo, se identificaron diferencias en la interpretación. El modelo qwen3.5:4b reconoció correctamente la mayoría de los datos faltantes, mientras que qwen3.5:0.8b presentó dificultades en algunos casos, como la hora de recogida de los jugos.

También se observó que un JSON válido no garantiza que todos los datos extraídos sean correctos, ya que el modelo puede generar una estructura válida y aun así interpretar incorrectamente la información.



3\. ¿Qué casos fallaron en V1, pero no en V2?

Con el modelo qwen3.5:4b, la versión V1 presentó errores en los casos 3, 6 y 10. Estos correspondían a una consulta de recomendación, una intención de cancelar un pedido y un reclamo por un pedido que no aparecía.

Con el modelo qwen3.5:0.8b, la versión V1 falló en los casos 4 y 6. El primero correspondía a una consulta sobre los horarios para realizar pedidos y el segundo a una intención de cancelación.

Al utilizar la versión V2, estos errores fueron corregidos. Sin embargo, el modelo qwen3.5:0.8b continuó fallando en el caso 3, confundiendo una consulta de recomendación con un pedido.



4\. Conclusión



Los resultados muestran que la versión V2 es más efectiva que la V1 para clasificar los mensajes de CafeFET. Las definiciones y los ejemplos permiten que los modelos comprendan mejor las categorías y reduzcan los errores de interpretación.

El modelo qwen3.5:4b obtuvo el mejor resultado, alcanzando un 100 % de aciertos con la versión V2. Por su parte, qwen3.5:0.8b alcanzó un 90 %.

Por lo tanto, para este conjunto de pruebas, se considera que la combinación de qwen3.5:4b y el prompt V2 ofrece el mejor desempeño.

