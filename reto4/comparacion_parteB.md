Comparación de la Parte B – Instrucciones y contexto



En esta prueba se comparó el comportamiento de Qwen utilizando una instrucción de formato de dos maneras: primero, mediante un mensaje normal dentro de la conversación y, después, mediante la configuración del mensaje del sistema con `/set system`.



Primera prueba: instrucción como mensaje normal



Al principio, se le indicó al modelo que todas sus respuestas debían comenzar con la palabra `VEREDICTO:`. En la primera pregunta, el modelo cumplió la instrucción y comenzó su respuesta correctamente.



Sin embargo, en la segunda pregunta ya no comenzó con esa palabra. Esto mostró que la instrucción no se mantuvo durante toda la prueba. Es importante aclarar que la sesión de Ollama se cerró accidentalmente y se inició nuevamente antes de realizar esa segunda pregunta. Por esta razón, no se puede afirmar que el olvido se debió únicamente al límite de contexto, ya que el reinicio también pudo ocasionar la pérdida del historial de la conversación.



Segunda prueba: instrucción mediante `/set system`



En esta prueba se limpió el historial con `/clear`, se configuró nuevamente el contexto de 512 tokens y se estableció la regla mediante `/set system`.



El modelo comenzó sus dos respuestas con la palabra `VEREDICTO:`, por lo que mantuvo la instrucción de formato durante esta prueba.



A pesar de seguir la instrucción, el modelo agregó información que no estaba en las reglas de CafeFET. Esto demuestra que respetar el formato solicitado no garantiza que toda la información de la respuesta sea correcta.



Comparación de resultados



En la primera prueba, el modelo siguió la instrucción inicialmente, pero dejó de hacerlo en la segunda respuesta. En cambio, cuando la regla se estableció mediante `/set system`, la conservó en las dos respuestas.



También se observó que en ambas pruebas el modelo agregó información que no correspondía a las reglas originales de CafeFET.



Conclusión



La prueba permitió observar que la forma en que se proporciona una instrucción puede influir en su permanencia durante una conversación. Cuando se dio como un mensaje normal, el modelo la siguió inicialmente, pero después dejó de cumplirla. En cambio, al establecerla mediante `/set system`, conservó el formato solicitado en las dos respuestas.



No se puede atribuir con total seguridad la pérdida de la instrucción de la primera prueba solamente al límite de contexto de 512 tokens, debido al reinicio accidental de la sesión. Aun así, la comparación permitió identificar la diferencia entre proporcionar una instrucción dentro del chat y establecerla como mensaje del sistema.

