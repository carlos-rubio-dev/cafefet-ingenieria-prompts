Corrección de la cadena de prompts



1\. Primer paso: historia de usuario



El primer prompt generó correctamente la historia de usuario a partir del requisito de CafeFET. La respuesta respetó el formato solicitado: Como…, quiero…, para… No fue necesario realizar correcciones.



2\. Segundo paso: criterios de aceptación



En la primera ejecución, el modelo inventó elementos que no estaban especificados en el requisito, como una sección llamada "Últimos Pedidos" y la prohibición de modificar los productos.



Se corrigió el prompt agregando restricciones para evitar nombres de secciones, botones y funcionalidades no especificadas.



En la segunda ejecución, la respuesta mejoró, pero todavía incluyó algunas suposiciones, como que el pedido anterior debía haberse realizado dentro del horario de atención y que no se podían modificar los productos.



3\. Tercer paso: casos de prueba



En la primera ejecución, el modelo generó una tabla que cubría los cuatro criterios de aceptación, pero incluyó condiciones adicionales, como impedir modificar o eliminar productos.



Se corrigió el prompt agregando restricciones para utilizar únicamente comportamientos respaldados por los criterios de aceptación.



En la segunda ejecución, se mantuvo la cobertura de los cuatro criterios y se conservaron los casos positivos y negativos. Sin embargo, persistió la suposición de que no se permitían modificaciones en el pedido repetido.



4\. Conclusión



La actividad permitió comprobar que dividir un requisito en varios prompts facilita la generación de historias de usuario, criterios de aceptación y casos de prueba.



También se observó que agregar restricciones mejora las respuestas del modelo, aunque no garantiza que desaparezcan todas las suposiciones. Por esta razón, es importante revisar y validar cada resultado antes de utilizarlo.

