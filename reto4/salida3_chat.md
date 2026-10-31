VEREDICTO: El proceso de creación de pedidos en CafeFET debe funcionar como un sistema robusto de control de flujo que priorice la integridad 

financiera, la gestión eficiente de recursos y la experiencia del usuario estudiantil. Para lograr esto, el sistema no debe permitir la finalización de 

una transacción hasta que se hayan verificado exhaustivamente todos los parámetros críticos antes de cualquier deducción de saldo o reserva de 

inventario. La primera validación fundamental es la disponibilidad de productos en tiempo real; el sistema debe consultar la base de datos de stock para 

asegurar que cada ítem seleccionado por el estudiante tenga un número de unidades positivo y suficiente para cubrir la cantidad solicitada. Esta 

verificación es crucial porque evita situaciones donde un pedido se procesa parcialmente o falla inmediatamente después, lo cual generaría frustración 

en el cliente y complicaciones operativas para los empleados del local. Si un producto no está disponible, el sistema debe bloquear la creación del 

pedido completo y notificar al usuario específicamente qué artículos faltan, permitiendo que modifique su selección antes de proceder.



La segunda validación indispensable es el cálculo dinámico del saldo del estudiante. El sistema debe sumar el precio total de todos los productos 

seleccionados y compararlo inmediatamente con el saldo disponible registrado en la cuenta del alumno. Es vital realizar esta comprobación porque CafeFET 

opera bajo un modelo de crédito estudiantil limitado; sin ella, se podrían generar deudas no autorizadas o intentos de pago fallidos que dañan la 

reputación del sistema. Cuando el saldo sea insuficiente para cubrir el costo total, el proceso debe detenerse automáticamente y presentar al estudiante 

una alerta clara indicando cuánto falta para completar la compra, sugiriendo opciones como añadir fondos o reducir la cantidad de productos.



Tercero, el sistema debe validar estrictamente los horarios de atención y los días permitidos de operación. CafeFET no funciona 24 horas ni todos los 

días de la semana; por lo tanto, el módulo de pedidos debe estar programado para aceptar solicitudes únicamente dentro de las franjas horarias 

operativas definidas y en los días hábiles autorizados. Ignorar esta regla llevaría a un malentendido sobre la capacidad del local para atender al 

momento, resultando en una espera innecesaria o un cierre inesperado. Si el intento de pedido se realiza fuera de horario o en un día cerrado, el 

sistema debe rechazar la solicitud desde el inicio con un mensaje informativo que aclare los horarios reales de servicio.



Finalmente, todas estas validaciones deben ocurrir secuencialmente y de manera atómica; es decir, si alguna condición falla, ninguna deducción de saldo 

ni reserva de stock debe realizarse. El estado del pedido debe permanecer como "pendiente de revisión" o ser cancelado inmediatamente sin generar 

registros financieros erróneos. La importancia de este enfoque radica en la prevención de errores humanos y la automatización de la confianza del 

usuario; al garantizar que todas las reglas se cumplan antes de aceptar el pedido, CafeFET asegura un funcionamiento transparente, justo y eficiente 

para toda la comunidad estudiantil, manteniendo la solidez de sus recursos y la satisfacción de sus clientes.

