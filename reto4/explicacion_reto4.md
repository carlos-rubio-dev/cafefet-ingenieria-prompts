Reto 4 – Razonar y manejar el contexto


Parte A: Cadena de pensamiento


En esta parte se utilizó el modelo `phi-demo` para analizar una función de CafeFET que contenía errores en sus validaciones.

Primero se realizó una pregunta breve para identificar por qué la función permitía un pedido inválido. Después se solicitó una evaluación paso a paso utilizando datos concretos, indicando el valor de cada condición y si el programa continuaba o devolvía `False`.

En la primera respuesta, el modelo identificó algunos problemas de la función, pero no propuso correctamente el límite máximo de productos. En la segunda respuesta realizó los cálculos de las condiciones y explicó cómo se ejecutaba la función. Sin embargo, tampoco detectó que un pedido de seis productos incumple la regla de CafeFET, que permite un máximo de cinco.

Esto permitió observar que solicitar un análisis paso a paso ayuda a revisar las condiciones y los valores utilizados, pero no garantiza que el modelo interprete correctamente todas las reglas del negocio.


Parte B: Instrucciones y contexto
En esta parte se utilizó `qwen-demo` con un contexto de 512 tokens. El objetivo fue comprobar si el modelo conservaba una instrucción de formato durante una conversación.
Primero se le indicó mediante un mensaje normal que todas sus respuestas debían comenzar con la palabra `VEREDICTO:`. En la primera respuesta cumplió la instrucción, pero en la segunda no la conservó. Durante esta prueba se cerró accidentalmente la sesión y se inició nuevamente, por lo que no se puede asegurar que el olvido se debiera solamente al límite de contexto.
Después se repitió la prueba configurando la misma regla mediante `/set system`. En esta ocasión, el modelo comenzó sus dos respuestas con la palabra `VEREDICTO:`, lo que mostró una mayor conservación de la instrucción durante esa sesión.
También se identificó que el modelo agregó información que no estaba en las reglas originales de CafeFET. Por esta razón, sus respuestas deben revisarse antes de utilizarlas.

Relación con la ventana de contexto
La ventana de contexto es el espacio limitado de información que el modelo puede utilizar durante una conversación. En este espacio se incluyen las instrucciones y los mensajes anteriores. Cuando el historial supera el límite establecido, el sistema puede descartar los mensajes más antiguos para permitir que continúe la conversación. Por esta razón, una instrucción enviada como mensaje normal puede dejar de estar disponible. En cambio, el mensaje del sistema tiene un tratamiento especial, ya que se conserva durante el manejo del contexto. Esto permite mantener reglas importantes, como el formato que debe cumplir cada respuesta. Sin embargo, el experimento realizado no permite confirmar por completo el recorte de contexto, debido al reinicio accidental de la primera sesión.

Conclusión general
El reto permitió comprender que las instrucciones claras y el manejo del contexto son importantes al trabajar con modelos de lenguaje. Solicitar una evaluación detallada facilita la revisión de los resultados, mientras que establecer reglas mediante el mensaje del sistema puede ayudar a mantener instrucciones importantes durante una conversación.
Sin embargo, los modelos pueden cometer errores, interpretar incorrectamente las reglas o agregar información que no fue proporcionada. Por eso, sus respuestas deben verificarse con los requisitos originales del problema.


